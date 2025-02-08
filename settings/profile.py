from dataclasses import dataclass

from settings.settings import Settings

DEFAULT_NAME = 'default_mqtt_user'
PROFILES_PATH = 'settings/profiles.ini'


@dataclass
class Profile:
    _profile_id: str
    _name: str | None = None
    _host: str | None = None
    _port: str | None = None
    _client_id: str | None = None
    _username: str | None = None
    _password: str | None = None
    _ssl_tls: bool | None = None
    _ssl: str | None = None
    _ca_file: str | None = None
    _crt_file: str | None = None
    _key_file: str | None = None
    settings: Settings = Settings(PROFILES_PATH)
    is_created: bool = False

    def _set_field(self, key, value):
        """Setting field in instance and in profiles.ini"""
        if hasattr(self, '_' + key):
            setattr(self, '_' + key, value)
        else:
            raise AttributeError(f"Attribute '{key}' does not exist in the instance.")

        if self.is_created:
            self.settings.set_with_save(self.profile_id, str(key), str(value))

    def set_settings(self, settings: dict) -> None:
        for key, value in settings.items():
            self._set_field(key, value)

    def create(self) -> None:
        """Creating profile in profiles.ini."""
        if self.settings.has_section(self.name):
            raise ValueError(f'Profile with name "{self.name}" already exists')

        self.settings.add_section_with_save(self.name)
        self.is_created = True

        # TODO: add exception if error -> remove added fields
        for attr_name in dir(self):
            attr = getattr(type(self), attr_name, None)
            if isinstance(attr, property):
                self.settings.set_with_save(
                    self._name, attr_name, str(getattr(self, attr_name))
                )

    def delete(self): ...

    @property
    def profile_id(self):
        return self._profile_id

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
