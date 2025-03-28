import configparser
import os

from settings.profile import PROFILES_PATH, Profile
from settings.settings import Settings, create_ini_file, get_path
from settings.settings_utils import bool_param
from settings.topic import Topic

SETTINGS_PATH = 'settings/app_settings.ini'

class AppSettings:
    def __init__(self):
        self._settings_ini: Settings = Settings(SETTINGS_PATH)
        self._set_settings_from_ini()
        self._logger = False
        self._logger_quantity = 20
        self._logger_path = get_path('logs/')

    def _set_settings_from_ini(self):
        for setting in self._settings_ini.items('settings'):
            setattr(self, setting[0], setting[1])

    @property
    def logger(self):
        return self._logger

    @logger.setter
    @bool_param
    def logger(self, value: bool):
        self._logger = value

    @property
    def logger_quantity(self):
        return self._logger_quantity

    @logger_quantity.setter
    def logger_quantity(self, value: int | str):
        self._logger_quantity = int(value)

    @property
    def logger_path(self):
        return self._logger_path

    @logger_path.setter
    def logger_path(self, value: int | str):
        self._logger_path = value

app_settings = AppSettings()