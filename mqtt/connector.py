from datetime import datetime

from paho.mqtt.client import MQTT_ERR_SUCCESS, Client, ssl
from PyQt5.QtCore import QObject, pyqtSignal

from settings.profile import Profile


class MQTTConnector:
    def __init__(self):
        self.client = None
        self.profile = None
        self.topics = []

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

    def on_connect(self, _, __, ___, rc):
        if rc == 0:
            print(f'Successfully connected to {self.profile.host}:{self.profile.port}')
            for topic in self.topics:
                print(f'Topic: {topic.address}')
                self.client.subscribe(topic.address)
        else:
            print(f'Connection failed with code {rc}')

    @staticmethod
    def on_disconnect(_, __, rc):
        print(f"Client disconnected. Return code: {rc}")

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
        self.client.loop_stop()
        self.client.disconnect()
        print("Client stopped.")

    def publish(self, topic, message):
        if not topic:
            print('No topic to publish')
            return None

        result = self.client.publish(topic.address, message)
        if result.rc == MQTT_ERR_SUCCESS:
            print(f"Message sent to {topic.address}: {message}")
        else:
            print("Failed to send message.")

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic.address)
        print('unsubscribe successful')


class MQTTMixin(QObject, MQTTConnector):
    message_received = pyqtSignal(str, str)
    notification_signal = pyqtSignal(str)

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
            self.notification_signal.emit('Successfully connected!')
            for topic in self.topics:
                print(f'Topic: {topic.address}')
                self.client.subscribe(topic.address)
