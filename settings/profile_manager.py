import configparser
import os

from settings.profile import PROFILES_PATH, Profile
from settings.settings import Settings, create_ini_file


class ProfileManager:
    def __init__(self):
        self._profiles_ini: Settings = Settings('settings/profiles/profiles.ini')
        self._profiles = {}
        self.__profiles_from_ini()
        self.current_profile: Profile = self.get_current_profile()

    def __profiles_from_ini(self):
        for filename in os.listdir(PROFILES_PATH):
            if filename.endswith('.ini') and not filename == 'profiles.ini':
                filepath = os.path.join(PROFILES_PATH, filename)
                profile_file = configparser.ConfigParser()
                profile_file.read(filepath, encoding='utf-8')
                profile_id = os.path.splitext(filename)[0]
                mqtt_settings, clipboard = {}, {}

                for section in profile_file.sections():
                    if section == 'mqtt_settings':
                        for key, value in profile_file[section].items():
                            mqtt_settings['_' + key] = value

                    if section == 'clipboard':
                        for key, value in profile_file[section].items():
                            clipboard[key] = value

                self._profiles[profile_id] = Profile(
                    profile_id, **mqtt_settings, clipboard=clipboard, is_created=True
                )

    def _generate_profile_id(self):
        existing_numbers = [
            int(name.split("_")[1])
            for name in self._profiles.keys()
            if name.startswith("profile_") and name.split("_")[1].isdigit()
        ]
        next_number = max(existing_numbers, default=0) + 1
        return f"profile_{next_number:02d}"

    def create_profile(self, **kwargs):
        profile_id = self._generate_profile_id()
        profile_ini = Settings(
            create_ini_file(profile_id, PROFILES_PATH, {'mqtt_settings': kwargs})
        )
        profile_ini.add_section_with_save('clipboard')

        profile = Profile(profile_id)
        profile.name = kwargs.get('name')
        profile.create()
        profile.set_settings(kwargs)
        self.switch_profile(profile.profile_id)
        self._profiles[profile.name] = profile

        return profile

    def get_profile_by_id(self, profile_id) -> Profile:
        return self._profiles[profile_id]

    def set_profile_settings(self, profile_name, **kwargs):
        profile = self.get_profile_by_id(profile_name)
        profile.set_settings(kwargs)

    def get_current_profile(self):
        profile_id = self._profiles_ini.get('current_profile', 'current')
        return self.get_profile_by_id(profile_id)

    def switch_profile(self, profile_id):
        self._profiles_ini.set_with_save('current_profile', 'current', profile_id)
        self.current_profile = profile_id

    def delete_profile(self, profile_name):
        # TODO: dont forget delete from current and set some another
        profile = self.get_profile_by_id(profile_name)
        profile.delete()
        del self._profiles[profile]
        ...

    @property
    def profiles(self):
        return self._profiles


profile_manager = ProfileManager()
