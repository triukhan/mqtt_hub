import configparser
import os

from settings.profile import PROFILES_PATH, Profile
from settings.settings import Settings, create_ini_file, get_path
from settings.topic import Topic


class ProfileManager:
    def __init__(self):
        self._profiles_ini: Settings = Settings(PROFILES_PATH + 'profiles.ini')
        self._profiles = {}
        self.__profiles_from_ini()
        self.topic_to_publish = None

    @property
    def current_profile(self) -> Profile:
        return self.get_current_profile()

    def __profiles_from_ini(self):
        for filename in os.listdir(get_path(PROFILES_PATH)):
            if filename.endswith('.ini') and not filename == 'profiles.ini':
                filepath = get_path(os.path.join(PROFILES_PATH, filename))
                profile_file = configparser.ConfigParser()
                profile_file.read(filepath, encoding='utf-8')
                profile_id = os.path.splitext(filename)[0]
                clipboard, topics = {}, []

                profile = Profile(
                    profile_id,
                    clipboard=clipboard,
                    _topics=topics,
                    is_created=True,
                )

                for section in profile_file.sections():
                    if section == 'mqtt_settings':
                        for key, value in profile_file[section].items():
                            if key == 'is_default':
                                continue
                            setattr(profile, key, value)

                    if section == 'clipboard':
                        for key, value in profile_file[section].items():
                            clipboard[key] = value

                    if section == 'topics':
                        for _, topic_address in profile_file[section].items():
                            topic_settings = {}
                            for key, value in profile_file[topic_address].items():
                                topic_settings['_' + key] = value
                            topic = Topic(filepath, **topic_settings)
                            topics.append(topic)

                profile.clipboard = clipboard
                profile._topics = topics
                self._profiles[profile_id] = profile

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
        profile_ini.add_section_with_save('topics')

        profile = Profile(profile_id)
        profile.name = kwargs.get('name')
        profile.create()
        profile.set_settings(kwargs)
        self._profiles[profile.id] = profile
        self.switch_profile(profile.id)

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

    def delete_current_profile(self):
        self.current_profile.delete()
        del self._profiles[self.current_profile.id]
        self.switch_profile('profile_00')

    @property
    def profiles(self):
        return self._profiles


profile_manager = ProfileManager()
