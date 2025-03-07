from datetime import datetime

from paho.mqtt.client import MQTT_ERR_SUCCESS, Client, ssl
from PyQt5.QtCore import QObject, pyqtSignal

from settings.profile import Profile


class MQTTConnector:
    def __init__(self):
        self.client = None
        self.profile = None
        self.topics = []
        self.is_connected = False

    def setup_mqtt_settings(self):
        # TODO: rename
        if self.profile.ssl_tls == 'True':
            self.client.tls_set(
                ca_certs=self.profile.ca_file,
                certfile=self.profile.crt_file,
                keyfile=self.profile.key_file,
                tls_version=ssl.PROTOCOL_TLS,
            )

    def on_message(self, client, userdata, msg): ...

    def on_connect(self, _, __, ___, rc): ...

    def on_disconnect(self, _, __, rc): ...

    def start(self, profile: Profile):
        self.profile = profile
        self.topics = profile.topics
        self.client = Client(self.profile.client_id)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        self.setup_mqtt_settings()
        self.client.connect(self.profile.host, int(self.profile.port), keepalive=60)
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
        if not topic:
            print('No topic to publish')
            return None

        result = self.client.publish(topic.address, message)
        if result.rc == MQTT_ERR_SUCCESS:
            print(f"Message sent to {topic.address}: {message}")
        else:
            print("Failed to send message.")

    def subscribe(self, topic):
        self.client.subscribe(topic.address)
        print('Subscribe successful:', topic.address)

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic.address)
        print('Unsubscribe successful')


class MQTTMixin(QObject, MQTTConnector):
    message_received = pyqtSignal(str, str)
    notification_signal = pyqtSignal(str)
    connected_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def on_message(self, _, __, msg):
        received_payload = msg.payload.decode()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{timestamp}\n\n{received_payload}"
        self.message_received.emit(msg.topic, formatted_message)
        print(formatted_message)

    def on_connect(self, _, __, ___, rc):
        if rc == 0:
            self.handle_connect(True)
            for topic in self.topics:
                self.subscribe(topic)
        else:
            self.notification_signal.emit(f'MQTT Error. Return code: {rc}')

    def on_disconnect(self, _, __, rc):
        if rc == 0:
            self.handle_connect(False)
            print(f"Client disconnected. Return code: {rc}")
        else:
            self.notification_signal.emit(f'MQTT Error. Return code: {rc}')

    def handle_connect(self, connect: bool):
        self.is_connected = connect
        prefix = '' if self.is_connected else 'dis'
        self.notification_signal.emit(f'Successfully {prefix}connected')
        self.connected_signal.emit(self.is_connected)
