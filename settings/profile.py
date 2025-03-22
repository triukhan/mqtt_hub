from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import paho.mqtt.client as mqtt

from settings.settings import Settings, get_path
from settings.settings_utils import bool_param
from settings.topic import Topic

DEFAULT_NAME = 'default_mqtt_user'
PROFILES_PATH = 'settings/profiles/'


@dataclass
class Profile:
    _id: str
    _name: str | None = None
    _host: str | None = None
    _port: str | None = None
    _client_id: str | None = None
    _username: str | None = None
    _password: str | None = None
    _ssl_tls: bool | None = None
    _ssl: str | None = None
    _ca_signed: bool | None = None
    _self_signed: bool | None = None
    _ca_file: str | None = None
    _crt_file: str | None = None
    _key_file: str | None = None
    _mqtt_version: str | None = None
    _connect_timeout: int | None = None
    _keep_alive: int | None = None
    _auto_reconnect: bool | None = None
    _reconnect_period: int | None = None
    _clean_start: bool | None = None
    _session_expiry_interval: int | None = None
    _receive_maximum: int | None = None
    _maximum_packet_size: int | None = None
    _topics: list | None = field(default_factory=list)
    _is_default: bool | None = None
    clipboard: dict = defaultdict
    is_created: bool = False
    _convertor: str | None = 'JSON'
    _autoscroll: bool | None = False
    _clipboard_convertor: str | None = 'JSON'

    def __post_init__(self):
        self.profile_ini = get_path(f'{PROFILES_PATH}{self._id}.ini')
        self.settings = Settings(self.profile_ini)

        if not isinstance(self._topics, list):
            raise TypeError("_topics must be a list")

    def _set_field(
        self, key: str, value, only_ini: bool = False, section: str = 'mqtt_settings'
    ):
        """Setting field in instance and in profile.ini"""
        if not only_ini:
            if hasattr(self, '_' + key):
                setattr(self, '_' + key, value)
            else:
                raise AttributeError(
                    f"Attribute '{key}' does not exist in the instance."
                )

        if self.is_created:
            self.settings.set_with_save(section, key, value)

    def set_settings(self, settings: dict) -> None:
        for key, value in settings.items():
            self._set_field(key, value)

    def create(self) -> None:
        """Creating profile."""
        self.is_created = True

        # TODO: add exception if error -> remove added fields
        for attr_name in dir(self):
            if attr_name in ('id', 'topics'):
                continue
            attr = getattr(type(self), attr_name, None)
            if isinstance(attr, property):
                self.settings.set_with_save(
                    'mqtt_settings', attr_name, str(getattr(self, attr_name))
                )

    def delete(self):
        Path(get_path(self.profile_ini)).unlink()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name or 'No Name'

    @name.setter
    def name(self, name):
        # TODO: add logic deletion section with old name, adding section with new name
        self._set_field('name', name)

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host_address: str):
        self._set_field('host', host_address)

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port: id):
        self._set_field('port', port)

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        self._set_field('client_id', client_id)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username: str):
        self._set_field('username', username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._set_field('password', password)

    @property
    def ssl(self):
        return self._ssl

    @ssl.setter
    @bool_param
    def ssl(self, ssl: bool):
        self._set_field('ssl', ssl)

    @property
    def ssl_tls(self):
        return self._ssl

    @ssl_tls.setter
    @bool_param
    def ssl_tls(self, ssl_tls: bool):
        self._set_field('ssl_tls', ssl_tls)

    @property
    def ca_file(self):
        return self._ca_file

    @ca_file.setter
    def ca_file(self, path: str):
        self._set_field('ca_file', path)

    @property
    def crt_file(self):
        return self._crt_file

    @crt_file.setter
    def crt_file(self, path: str):
        self._set_field('crt_file', path)

    @property
    def key_file(self):
        return self._key_file

    @key_file.setter
    def key_file(self, path: str):
        self._set_field('key_file', path)

    @property
    def ca_signed(self):
        return self._ca_signed

    @ca_signed.setter
    @bool_param
    def ca_signed(self, value: bool):
        self._set_field('ca_signed', value)

    @property
    def self_signed(self):
        return self._self_signed

    @self_signed.setter
    @bool_param
    def self_signed(self, value: bool):
        self._set_field('self_signed', value)

    @property
    def mqtt_version(self):
        if not self._mqtt_version or self._mqtt_version == '3.1.1':
            return mqtt.MQTTv311
        if self._mqtt_version == '3.1':
            return mqtt.MQTTv31
        if self._mqtt_version == '5.0':
            return mqtt.MQTTv5

    @mqtt_version.setter
    def mqtt_version(self, value: str):
        self._set_field('mqtt_version', value)

    @property
    def connect_timeout(self):
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, value: int):
        self._set_field('connect_timeout', value)

    @property
    def keep_alive(self):
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, value: int):
        value = 60 if not value else value
        self._set_field('keep_alive', value)

    @property
    def auto_reconnect(self):
        return self._auto_reconnect

    @auto_reconnect.setter
    @bool_param
    def auto_reconnect(self, value: bool):
        self._set_field('auto_reconnect', value)

    @property
    def reconnect_period(self):
        return self._reconnect_period

    @reconnect_period.setter
    def reconnect_period(self, value: int):
        self._set_field('reconnect_period', value)

    @property
    def clean_start(self):
        return self._clean_start

    @clean_start.setter
    @bool_param
    def clean_start(self, value: bool):
        self._set_field('clean_start', value)

    @property
    def session_expiry_interval(self):
        return self._session_expiry_interval

    @session_expiry_interval.setter
    def session_expiry_interval(self, value: int):
        self._set_field('session_expiry_interval', value)

    @property
    def receive_maximum(self):
        return self._receive_maximum

    @receive_maximum.setter
    def receive_maximum(self, value: int):
        self._set_field('receive_maximum', value)

    @property
    def maximum_packet_size(self):
        return self._maximum_packet_size

    @maximum_packet_size.setter
    def maximum_packet_size(self, value: int):
        self._set_field('maximum_packet_size', value)

    @property
    def convertor(self):
        return self._convertor

    @convertor.setter
    def convertor(self, value: str):
        self._set_field('convertor', value)

    @property
    def autoscroll(self):
        return self._autoscroll

    @autoscroll.setter
    @bool_param
    def autoscroll(self, value: str):
        self._set_field('autoscroll', value)

    @property
    def topics(self):
        return self._topics

    @property
    def is_default(self):
        return self._is_default

    @property
    def clipboard_convertor(self):
        return self._clipboard_convertor

    @clipboard_convertor.setter
    def clipboard_convertor(self, value: str):
        self._set_field('clipboard_convertor', value)

    def add_clipboard(self, message_name: str, message_text: str):
        message_with_id = (
            message_name + '_ID_STARTS_HERE_' + str(len(self.clipboard) + 1)
        )
        self.clipboard[message_with_id] = message_text
        self.settings.set_with_save('clipboard', message_with_id, message_text)
        return message_with_id

    def edit_clipboard(
        self, start_data, msg_id: str, message_name: str, message_text: str
    ):
        if start_data[0] != message_name:
            del self.clipboard[msg_id]
            self.settings.remove_option('clipboard', msg_id)
            msg_id = message_name + '_ID_STARTS_HERE_' + str(len(self.clipboard) + 2)

        self.clipboard[msg_id] = message_text
        self.settings.set_with_save('clipboard', msg_id, message_text)

        return [message_text, [message_name, msg_id]]

    def delete_clipboard(self, message_name: str):
        del self.clipboard[message_name]
        self.settings.remove_option('clipboard', message_name)

    def add_topic(self, topic_settings: dict):
        if topic_address := topic_settings.get('_address') in self._topics:
            raise AttributeError(f'{topic_address} already exists')
        topic = Topic(self.profile_ini, **topic_settings)
        topic.create()
        self._topics.append(topic)
        return topic

    def delete_topic(self, topic):
        if topic in self._topics:
            self._topics.remove(topic)
        self.settings.remove_section(topic.address)
        self.settings.remove_option('topics', topic.address)

    def find_topic_by_address(self, address: str):
        for topic in self._topics:
            if topic.address == address:
                return topic
