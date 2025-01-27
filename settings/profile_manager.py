from settings.profile import PROFILES_PATH, Profile
from settings.settings import Settings


class ProfileManager:
    def __init__(self):
        self._profiles_ini: Settings = Settings(PROFILES_PATH)
        self._profiles = {}
        self.__profiles_from_ini()
        self.current_profile: Profile = self.get_current_profile()

    def __profiles_from_ini(self):
        for profile_name in self._profiles_ini.sections():
            if profile_name != 'current_profile':
                attributes_dict = {
                    '_' + key: value
                    for key, value in self._profiles_ini.items(profile_name)
                }
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
        profile_name = self._profiles_ini.get('current_profile', 'current')
        return self.get_profile_by_name(profile_name)

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
