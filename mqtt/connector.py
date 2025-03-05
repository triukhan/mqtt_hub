from datetime import datetime

from paho.mqtt.client import MQTT_ERR_SUCCESS, Client, ssl
from PyQt5.QtCore import QObject, pyqtSignal

from settings.profile_manager import profile_manager


class MQTTConnector:
    def __init__(self):
        self.client = Client(profile_manager.current_profile.client_id)
        self.topics = []

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def setup_mqtt_settings(self):
        # TODO: rename
        if profile_manager.current_profile.ssl_tls == 'True':
            self.client.tls_set(
                ca_certs=profile_manager.current_profile.ca_file,
                certfile=profile_manager.current_profile.crt_file,
                keyfile=profile_manager.current_profile.key_file,
                tls_version=ssl.PROTOCOL_TLS,
            )

    def on_connect(self, _, __, ___, rc):
        if rc == 0:
            print(f'Successfully connected to {profile_manager.current_profile.host}:{profile_manager.current_profile.port}')
            for topic in self.topics:
                print(f'Topic: {topic.address}')
                self.client.subscribe(topic.address)
        else:
            print(f'Connection failed with code {rc}')

    @staticmethod
    def on_disconnect(_, __, rc):
        print(f"Client disconnected. Return code: {rc}")

    def start(self, topics: list | None = None):
        self.topics = topics
        self.setup_mqtt_settings()
        self.client.connect(profile_manager.current_profile.host, int(profile_manager.current_profile.port), keepalive=60)
        self.client.loop_start()
        print('MQTT connection started in the background.')

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Client stopped.")

    def publish(self, message):
        if not profile_manager.topic_to_publish:
            print('No topic to publish')
            return None

        result = self.client.publish(profile_manager.topic_to_publish.address, message)
        if result.rc == MQTT_ERR_SUCCESS:
            print(
                f"Message sent to {profile_manager.topic_to_publish.address}: {message}"
            )
        else:
            print("Failed to send message.")


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
            self.notification_signal.emit(f'Successfully connected!')
            for topic in self.topics:
                print(f'Topic: {topic.address}')
                self.client.subscribe(topic.address)
