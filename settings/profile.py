from dataclasses import dataclass

from settings.settings import Settings

PROFILES_PATH = 'settings/profiles.ini'
DEFAULT_NAME = 'default_mqtt_user'


@dataclass
class Profile:
    _name: str
    _host: str | None = None
    _port: str | None = None
    settings: Settings = Settings(PROFILES_PATH)
    is_created: bool = False

    def set_field(self, key, value):
        """Setting field in instance and in profiles.ini"""
        if hasattr(self, '_' + key):
            setattr(self, '_' + key, value)
        else:
            raise AttributeError(f"Attribute '{key}' does not exist in the instance.")

        if self.is_created:
            self.settings.set_with_save(self.name, str(key), str(value))

    def set_settings(self, settings: dict) -> None:
        for key, value in settings.items():
            self.set_field(key, value)

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # TODO: add logic deletion section with old name, adding section with new name
        self.set_field('name', name)

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host_address: str):
        self.set_field('host', host_address)

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port: id):
        self.set_field('port', port)


class ProfileManager:
    def __init__(self):
        self._profiles_ini: Settings = Settings(PROFILES_PATH)
        self._profiles = {}
        self.__profiles_from_ini()
        self.current_profile: Profile = self.get_current_profile()

    def __profiles_from_ini(self):
        for profile_name in self._profiles_ini.sections():
            if profile_name != 'current_profile':
                attributes_dict = {'_' + key: value for key, value in self._profiles_ini.items(profile_name)}
                self._profiles[profile_name] = Profile(**attributes_dict)

    def create_profile(self, profile_name, **kwargs):
        profile = Profile(profile_name)
        profile.create()
        profile.set_settings(kwargs)
        self.switch_profile(profile.name)
        self._profiles[profile.name] = profile

    def get_profile_by_name(self, profile_name) -> Profile:
        return self._profiles[profile_name]

    def set_profile_settings(self, profile_name, **kwargs):
        profile = self.get_profile_by_name(profile_name)
        profile.set_settings(kwargs)

    def get_current_profile(self):
        return self._profiles_ini.get('current_profile', 'current')

    def switch_profile(self, profile_name):
        self._profiles_ini.set_with_save('current_profile', 'current', profile_name)
        self.current_profile = profile_name

    def delete_profile(self, profile_name):
        # TODO: dont forget delete from current and set some another
        profile = self.get_profile_by_name(profile_name)
        profile.delete()
        del self._profiles[profile]
        ...

    @property
    def profiles(self):
        return self._profiles
