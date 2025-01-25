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


@dataclass
class CurrentProfileHandler:
    """Class only to handle current profile"""

    settings: Settings = Settings(PROFILES_PATH)
    current_profile_name = settings.get('current_profile', 'current')

    def change_current_profile(self, profile_name):
        self.settings.set_with_save('current_profile', 'current', profile_name)


class ProfileManager:
    def __init__(self):
        self._profiles_ini: Settings = Settings(PROFILES_PATH)
        self._profiles = []
        self.__profiles_from_ini()
        self.current_handler = CurrentProfileHandler()


    def __profiles_from_ini(self):
        for profile_name in self._profiles_ini.sections():
            if profile_name != 'current_profile':
                self._profiles.append(Profile(profile_name, **self._profiles_ini.items(profile_name)))

    def create_profile(self, profile_name, **kwargs):
        profile = Profile(profile_name)
        profile.create()
        profile.set_settings(kwargs)
        self.switch_profile(profile.name)
        self._profiles.append(profile)

    def get_profile_by_name(self, profile_name) -> Profile: ...

    def set_profile_settings(self, profile_name, **kwargs):
        profile = self.get_profile_by_name(profile_name)
        profile.set_settings(kwargs)

    def switch_profile(self, profile_name):
        self.current_handler.change_current_profile(profile_name)

    def delete_profile(self, profile_name):
        # TODO: dont forget delete from current and set some another
        profile = self.get_profile_by_name(profile_name)
        profile.delete()
        self._profiles.remove(profile)
        ...

    @property
    def profiles(self):
        return self._profiles

    @property
    def current_profile(self):
        # TODO: instance, not name
        return self.current_handler.current_profile_name
