from settings.settings import Settings, get_path
from settings.settings_utils import bool_param

SETTINGS_PATH = 'settings/app_settings.ini'


class AppSettings:
    def __init__(self):
        self._settings_ini: Settings = Settings(SETTINGS_PATH)
        self._logger = False
        self._logger_quantity = 20
        self._logger_path = get_path('logs/')
        self._set_settings_from_ini()

    def _set_settings_from_ini(self):
        print(self._settings_ini.sections())
        for setting in self._settings_ini.items('settings'):
            setattr(self, setting[0], setting[1])

    @property
    def logger(self):
        return self._logger

    @logger.setter
    @bool_param
    def logger(self, value: bool):
        self._logger = value
        self._settings_ini.set_with_save('settings', 'logger', value)

    @property
    def logger_quantity(self):
        return self._logger_quantity

    @logger_quantity.setter
    def logger_quantity(self, value: int | str):
        self._logger_quantity = int(value)
        self._settings_ini.set_with_save('settings', 'logger_quantity', value)

    @property
    def logger_path(self):
        return self._logger_path

    @logger_path.setter
    def logger_path(self, value: int | str):
        if not value:
            value = get_path('logs/')

        if not value.endswith('/'):
            value += '/'
        self._logger_path = value
        self._settings_ini.set_with_save('settings', 'logger_path', value)


app_settings = AppSettings()
