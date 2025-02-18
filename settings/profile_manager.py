from settings.profile import PROFILES_PATH, Profile
from settings.settings import Settings

CLIPBOARD_PATH = 'settings/clipboard.ini'
PROFILESS_PATH = 'settings/profiles/'


class ProfileManager:
    def __init__(self):
        self._profiles_ini: Settings = Settings(PROFILES_PATH)
        self._clipboard_ini: Settings = Settings(CLIPBOARD_PATH)
        self._profiles = {}
        self.__profiles_from_ini()
        self.current_profile: Profile = self.get_current_profile()

    def __profiles_from_ini(self):
        for profile_id in self._profiles_ini.sections():
            if profile_id != 'current_profile':
                attributes_dict = {
                    '_' + key: value
                    for key, value in self._profiles_ini.items(profile_id)
                }
                self._profiles[profile_id] = Profile(
                    profile_id, **attributes_dict, is_created=True
                )

    def _generate_profile_id(self):
        existing_numbers = [
            int(name.split("_")[1])
            for name in self._profiles.keys()
            if name.startswith("profile_") and name.split("_")[1].isdigit()
        ]
        next_number = max(existing_numbers, default=0) + 1
        return f"profile_{next_number:02d}"

    def create_profile(self, profile_name, **kwargs):
        self.create_ini(profile_name, PROFILESS_PATH)
        profile_id = self._generate_profile_id()
        self._clipboard_ini.add_section_with_save(profile_id)
        profile = Profile(profile_id)
        profile.name = profile_name
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

    def add_clipboard_message(self, message_name: str, message_text: str):
        self._clipboard_ini.set_with_save(
            self.current_profile.name, message_name, message_text
        )

    def get_clipboard_messages(self):
        return self._clipboard_ini.get_section(self.current_profile.name)

    def create_ini(self, name, path, params: dict | None = None):
        if params:
            for section in params:
                self.config[section] = params[section]

        with open(f'{path}/{name}.ini', 'w') as configfile:
            self.config.write(configfile)

        return name


profile_manager = ProfileManager()
