from paho.mqtt.client import MQTT_ERR_SUCCESS, Client, ssl

from settings.profile_manager import ProfileManager


class MQTTConnector:
    def __init__(self, topics):
        self.profile_manager = ProfileManager()
        self.profile = self.profile_manager.current_profile
        if not self.profile.client_id:
            # TODO: make unnecessary
            raise ValueError('Client ID is not set')
        self.client = Client(self.profile.client_id)
        self.topics = topics

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def setup_mqtt_settings(self):
        # TODO: rename
        if self.profile.tls_enabled == 'True':
            self.client.tls_set(
                ca_certs=self.profile.ca_file,
                certfile=self.profile.crt_file,
                keyfile=self.profile.key_file,
                tls_version=ssl.PROTOCOL_TLS,
            )

    def on_connect(self, _, __, ___, rc):
        if rc == 0:
            print(f'Successfully connected to {self.profile.host}:{self.profile.port}')
            for topic in self.topics:
                print(f'Topic: {topic}')
                self.client.subscribe(topic)
        else:
            print(f'Connection failed with code {rc}')

    @staticmethod
    def on_disconnect(_, __, rc):
        print(f"Client disconnected. Return code: {rc}")

    @staticmethod
    def on_message(_, __, msg):
        print(f"Received message: {msg.payload.decode()} from topic: {msg.topic}")

    def start(self):
        self.setup_mqtt_settings()
        self.client.connect(self.profile.host, int(self.profile.port), keepalive=60)
        self.client.loop_start()
        print('MQTT connection started in the background.')

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Client stopped.")

    def publish(self, topic, message):
        result = self.client.publish(topic, message)
        if result.rc == MQTT_ERR_SUCCESS:
            print(f"Message sent to {topic}: {message}")
        else:
            print("Failed to send message.")
