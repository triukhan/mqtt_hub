import configparser
import os


class Settings:
    """Universal class to parse .ini files."""

    def __init__(self, settings_path):
        self.settings_path = settings_path
        self.config = configparser.ConfigParser()
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_path):
            self.config.read(self.settings_path, encoding="utf-8")
        else:
            raise ValueError("Settings file not found")

    def sections(self):
        return self.config.sections()

    def items(self, section):
        return self.config.items(section)

    def save_settings(self):
        with open(self.settings_path, "w") as f:
            self.config.write(f)

    def get_section(self, section):
        if self.config.has_section(section):
            return dict(self.config.items(section))

    def has_section(self, section):
        return self.config.has_section(section)

    def add_section_with_save(self, section):
        self.config.add_section(section)
        self.save_settings()

    def get(self, section, key, default=None):
        if self.config.has_section(section) and self.config.has_option(section, key):
            return self.config.get(section, key)
        return default

    def set_with_save(self, section, key, value):
        self.load_settings()
        if not self.config.has_section(section):
            raise ValueError(f'Section "{section}" does not exist')
        self.config.set(section, key, str(value))
        self.save_settings()

    def create_ini(self, name, path, params: dict | None = None):
        if params:
            for section in params:
                self.config[section] = params[section]

        with open(f'{path}/{name}.ini', 'w') as configfile:
            self.config.write(configfile)
        self.save_settings()

        return name
