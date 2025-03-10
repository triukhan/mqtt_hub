import os
from collections import defaultdict
from dataclasses import dataclass, field

from settings.settings import Settings, get_path
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
    _topic_alias_maximum: int | None = None
    _request_response: bool | None = None
    _request_problem_info: bool | None = None
    _topics: list | None = field(default_factory=list)
    _is_default: bool | None = None
    clipboard: dict = defaultdict
    is_created: bool = False

    def __post_init__(self):
        self.profile_ini = f'{PROFILES_PATH}{self._id}.ini'
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
        os.remove(get_path(self.profile_ini))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

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
    def ssl(self, ssl: bool):
        self._set_field('ssl', ssl)

    @property
    def ssl_tls(self):
        return self._ssl

    @ssl_tls.setter
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
    def ca_signed(self, value: bool):
        self._set_field('ca_signed', value)

    @property
    def self_signed(self):
        return self._self_signed

    @self_signed.setter
    def self_signed(self, value: bool):
        self._set_field('self_signed', value)

    @property
    def mqtt_version(self):
        return self._mqtt_version

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
        self._set_field('keep_alive', value)

    @property
    def auto_reconnect(self):
        return self._auto_reconnect

    @auto_reconnect.setter
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
    def topic_alias_maximum(self):
        return self._topic_alias_maximum

    @topic_alias_maximum.setter
    def topic_alias_maximum(self, value: int):
        self._set_field('topic_alias_maximum', value)

    @property
    def request_response(self):
        return self._request_response

    @request_response.setter
    def request_response(self, value: bool):
        self._set_field('request_response', value)

    @property
    def request_problem_info(self):
        return self._request_problem_info

    @request_problem_info.setter
    def request_problem_info(self, value: bool):
        self._set_field('request_problem_info', value)

    @property
    def topics(self):
        return self._topics

    @property
    def is_default(self):
        return self._is_default

    def add_clipboard(self, message_name: str, message_text: str):
        self.clipboard[message_name] = message_text
        self.settings.set_with_save('clipboard', message_name, message_text)

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
