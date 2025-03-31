import logging
from contextlib import suppress
from datetime import datetime

from paho.mqtt.client import MQTT_ERR_SUCCESS, Client, MQTTv5, SubscribeOptions, ssl
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties
from PyQt5.QtCore import QObject, QTimer, pyqtSignal

from connections.connection_utils import Result
from mqtt.connector_utils import convert_to_format, validate_start
from mqtt.logger import Logger
from settings.app_settings import app_settings
from settings.profile import Profile
from settings.profile_manager import profile_manager


class MQTTConnector:
    def __init__(self):
        self.client = None
        self.profile = None
        self.topics = []
        self.is_connected = False

    def setup_mqtt_settings(self):
        if self.profile.username:
            self.client.username_pw_set(username=self.profile.username)
        if self.profile.password:
            self.client.username_pw_set(password=self.profile.password)
        if self.profile.connect_timeout:
            self.client._connect_timeout = int(self.profile.connect_timeout)
        if not self.profile.auto_reconnect:
            self.client.reconnect_delay_set(min_delay=0, max_delay=0)
        if self.profile.auto_reconnect:
            self.client.reconnect_delay_set(
                min_delay=1, max_delay=self.profile.reconnect_period or '120'
            )
        if self.profile.ssl_tls:
            if self.profile.ssl:
                if self.profile.self_signed:
                    self.client.tls_set(
                        ca_certs=self.profile.ca_file,
                        certfile=self.profile.crt_file,
                        keyfile=self.profile.key_file,
                        tls_version=ssl.PROTOCOL_TLS,
                    )
                else:
                    self.client.tls_set()
            else:
                self.client.tls_set()

    def make_mqtt_kwargs(self):
        kwargs = {'keepalive': int(self.profile.keep_alive)}
        clean_session = {}

        if self.profile.mqtt_version == MQTTv5:
            properties = Properties(PacketTypes.CONNECT)
            prop = False

            if self.profile.receive_maximum:
                properties.ReceiveMaximum = int(self.profile.receive_maximum)
                prop = True
            if self.profile.maximum_packet_size:
                properties.MaximumPacketSize = int(self.profile.maximum_packet_size)
                prop = True
            if not self.profile.clean_start:
                kwargs['clean_start'] = False
                if self.profile.session_expiry_interval:
                    properties.SessionExpiryInterval = int(
                        self.profile.session_expiry_interval
                    )
                    prop = True
            if prop:
                kwargs['properties'] = properties
        else:
            clean_session['clean_session'] = self.profile.clean_start

        return kwargs, clean_session

    def on_message(self, client, userdata, msg): ...

    def on_connect(self, _, __, ___, rc, ____=None): ...

    def on_disconnect(self, _, __, rc, ___=None): ...

    def start(self, profile: Profile):
        self.profile = profile
        self.topics = profile.topics
        kwargs, clean_session = self.make_mqtt_kwargs()

        self.client = Client(
            self.profile.client_id, protocol=self.profile.mqtt_version, **clean_session
        )

        self.setup_mqtt_settings()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        self.client.connect_async(
            self.profile.host,
            int(self.profile.port),
            **kwargs,
        )
        self.client.loop_start()

    def stop(self):
        if self.is_connected:
            self.client.loop_stop()
            self.client.disconnect()
            print('Client stopped')
        else:
            print('Client not connected')

    def publish(self, topic, message):
        result = self.client.publish(topic.address, message)
        if result.rc != MQTT_ERR_SUCCESS:
            return f'Failed to send message. Result Code: {result.rc}'

    def subscribe(self, topic):
        settings = topic.get_options_dict()
        options = SubscribeOptions(**settings)
        self.client.subscribe(topic.address, options=options)
        print('Subscribe successful: ', topic.address, '. Settings: ', settings)

    def unsubscribe(self, topic):
        with suppress(AttributeError):
            self.client.unsubscribe(topic.address)
        print('Unsubscribe successful')


class MQTTMixin(QObject, MQTTConnector):
    message_received = pyqtSignal(str, str)
    connected_signal = pyqtSignal(bool)
    notification_signal = pyqtSignal(str, Result)

    def __init__(self):
        super().__init__()
        self.was_connected = False
        self.logger = None

    def on_message(self, _, __, msg):
        received_payload = convert_to_format(
            msg.payload.decode(), profile_manager.current_profile.convertor
        )
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f'{timestamp}\n\n{received_payload}'
        self.message_received.emit(msg.topic, formatted_message)

        if self.logger is not None:
            logging.info(f'Message received on topic {msg.topic}: {received_payload}')

    def on_connect(self, _, __, ___, rc, ____=None):
        if rc != 0:
            self.notification_signal.emit(f'MQTT Error. Return code: {rc}')
            return

        self.handle_connect(True)
        self.was_connected = True

        if app_settings.logger:
            self.logger = Logger(
                max_files=app_settings.logger_quantity,
                path=app_settings.logger_path,
                rc=rc,
            )
            self.logger.start_logger()

        for topic in self.topics:
            self.subscribe(topic)

    def on_disconnect(self, _, __, rc, ___=None):
        if rc != 0:
            self.notification_signal.emit(
                f'Disconnected with error. Return code: {rc}', Result.FAILURE
            )
            return
        self.handle_connect(False)
        if self.logger:
            self.logger.stop()
            self.logger = None

    def handle_connect(self, conn: bool):
        self.is_connected = conn

        prefix = '' if self.is_connected else 'dis'
        self.notification_signal.emit(f'{prefix}connected'.capitalize(), Result.SUCCESS)
        self.connected_signal.emit(self.is_connected)

    def start(self, profile: Profile):
        if (error_msg := validate_start(profile)) is not None:
            self.notification_signal.emit(error_msg, Result.FAILURE)
            return
        super().start(profile)

        self.was_connected = False
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(5000)

    def on_timeout(self):
        if not self.was_connected:
            self.notification_signal.emit(
                'Error: Connection timeout. Please check your settings', Result.FAILURE
            )
            self.connected_signal.emit(self.is_connected)

    def publish(self, topic, message):
        if not self.is_connected:
            self.notification_signal.emit(
                'Client is not connected. You need to start connection at first.',
                Result.COMMON,
            )
            return None

        if not topic:
            self.notification_signal.emit(
                'No topic to publish. Select topic by click on it.', Result.COMMON
            )
            return None

        res = super().publish(topic, message)

        if res is not None:
            self.notification_signal.emit(res, Result.FAILURE)
