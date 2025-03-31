from PyQt5.QtWidgets import QFileDialog

from settings.app_settings import app_settings
from UI.tabs.settings_tab_ui import SettingsTabUi


class SettingsTab(SettingsTabUi):
    def __init__(self):
        super().__init__()
        self._setup_common_connections()
        self.set_settings()

    def _setup_common_connections(self):
        self.logger_path_button.clicked.connect(
            lambda: self.open_folder_dialog(self.logger_path_field)
        )

    def save_settings(self):
        app_settings.logger = self.logger_checkbox.isChecked()
        app_settings.logger_quantity = self.logger_spin.text()
        app_settings.logger_path = self.logger_path_field.text()

    def set_settings(self):
        self.logger_checkbox.setChecked(app_settings.logger)
        self.logger_spin.setValue(app_settings.logger_quantity)
        self.logger_path_field.setText(app_settings.logger_path)

    def open_folder_dialog(self, field):
        options = QFileDialog.Options()
        folder = QFileDialog.getExistingDirectory(
            self, 'Choose Directory', '', options=options
        )
        if folder:
            field.setText(folder)
