import configparser
import os


def get_path(relative_path):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Settings:
    """Universal class to parse .ini files."""

    def __init__(self, settings_path: str | None = None):
        self.settings_path = get_path(settings_path)
        self.config = configparser.ConfigParser()
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_path):
            self.config.read(self.settings_path, encoding='utf-8')
        else:
            raise ValueError('Settings file not found')

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
        if not self.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))
        self.save_settings()

    def remove_section(self, section):
        self.load_settings()
        self.config.remove_section(section)
        self.save_settings()

    def remove_option(self, section, option):
        self.load_settings()
        if self.config.has_section(section):
            if self.config.has_option(section, option):
                self.config.remove_option(section, option)

        self.save_settings()

    def clear_section(self, section):
        self.load_settings()
        self.config[section].clear()
        self.save_settings()


def create_ini_file(filename: str, path: str, data: dict | None = None):
    config = configparser.ConfigParser()
    path = get_path(path)

    if data:
        for section, values in data.items():
            config[section] = {}
            for key, value in values.items():
                config[section][key] = str(value)

    full_path = os.path.join(path, filename + '.ini')
    with open(full_path, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

    return full_path
