import json
from datetime import datetime

from PyQt5.QtWidgets import QPlainTextEdit
from paho.mqtt.client import MQTT_ERR_SUCCESS, Client, MQTTv5, ssl
from PyQt5.QtCore import QObject, pyqtSignal

from UI.interface_utils import JsonHighlighter
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
                    self.client.tls_set()  # todo: resolve it
            else:
                self.client.tls_set()

    def on_message(self, client, userdata, msg): ...

    def on_connect(self, _, __, ___, rc): ...

    def on_disconnect(self, _, __, rc): ...

    def start(self, profile: Profile):
        self.profile = profile
        self.topics = profile.topics
        self.client = Client(self.profile.client_id, protocol=self.profile.mqtt_version)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        self.setup_mqtt_settings()
        self.client.connect(
            self.profile.host,
            int(self.profile.port),
            keepalive=int(self.profile.keep_alive),
        )
        self.client.loop_start()
        print('MQTT connection started in the background.')

    def stop(self):
        if self.is_connected:
            self.client.loop_stop()
            self.client.disconnect()
            print('Client stopped')
        else:
            print('Client not connected')

    def publish(self, topic, message):
        result = self.client.publish(topic.address, message)
        if result.rc == MQTT_ERR_SUCCESS:
            print(f'Message sent to {topic.address}: {message}')
        else:
            return f'Failed to send message. Result Code: {result.rc}'

    def subscribe(self, topic):
        self.client.subscribe(topic.address)
        print('Subscribe successful:', topic.address)

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic.address)
        print('Unsubscribe successful')


class MQTTMixin(QObject, MQTTConnector):
    message_received = pyqtSignal(str, str)
    connected_signal = pyqtSignal(bool)
    success_signal = pyqtSignal(str)
    fail_signal = pyqtSignal(str)
    common_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def on_message(self, _, __, msg):
        received_payload = convert_to_format(msg.payload.decode())
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp}\n\n{received_payload}"
        self.message_received.emit(msg.topic, formatted_message)
        print(formatted_message)

    def on_connect(self, _, __, ___, rc):
        if rc != 0:
            self.fail_signal.emit(f'MQTT Error. Return code: {rc}')
            return
        self.handle_connect(True)
        for topic in self.topics:
            self.subscribe(topic)

    def on_disconnect(self, _, __, rc):
        if rc != 0:
            self.fail_signal.emit(f'Disconnected with error. Return code: {rc}')
            return
        self.handle_connect(False)

    def handle_connect(self, conn: bool):
        self.is_connected = conn
        prefix = '' if self.is_connected else 'dis'
        self.common_signal.emit(f'{prefix}connected'.capitalize())
        self.connected_signal.emit(self.is_connected)

    def start(self, profile: Profile):
        if (error_msg := validate_start(profile)) is not None:
            self.fail_signal.emit(error_msg)
            return
        super().start(profile)

    def publish(self, topic, message):
        if not self.is_connected:
            self.common_signal.emit(
                'Client is not connected. You need to start connection at first.'
            )
            return None

        if not topic:
            self.common_signal.emit('No topic to publish. Select topic by click on it.')
            return None

        res = super().publish(topic, message)

        if res is not None:
            self.fail_signal.emit(res)


def convert_to_format(payload):
    f = profile_manager.current_profile.convertor

    if f == 'Plaintext':
        return payload

    try:
        json_obj = json.loads(payload)
        return json.dumps(json_obj, indent=4)
    except json.JSONDecodeError:
        return payload

def validate_start(profile: Profile):
    if not profile.host:
        return 'Error: Host is absent is settings'
    if not profile.port:
        return 'Error: Port is absent is settings'
    if not profile.client_id and profile.mqtt_version != MQTTv5:
        return 'Error: Client ID is absent is settings'
    if profile.self_signed and '' in (
            profile.ca_file,
            profile.crt_file,
            profile.key_file,
    ):
        return 'Error: Some certificates are absent is settings'
    return None
