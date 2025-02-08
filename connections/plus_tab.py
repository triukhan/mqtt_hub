from PyQt5.QtWidgets import QMessageBox

from GUI.tabs.plus_tab import PlusTabUI
from settings.profile_manager import ProfileManager


class PlusTab(PlusTabUI):
    def __init__(self):
        super().__init__()
        self.profile_manager = ProfileManager()
        self.current_profile = self.profile_manager.current_profile


class EditTab(PlusTabUI):
    def __init__(self):
        super().__init__()
        self.setup_connections()
        self.profile_manager = ProfileManager()
        self.current_profile = self.profile_manager.current_profile
        self.load_current_profile_settings()

    def setup_connections(self):
        self.client_cert_button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        QMessageBox.information(self, "Info", "Button clicked in Plus Tab!")

    def load_current_profile_settings(self):
        self.name_field.setText(self.current_profile.name)
        self.host_field.setText(self.current_profile.host)
        self.port_field.setText(self.current_profile.port)
        self.client_id_field.setText(self.current_profile.client_id)
        self.username_field.setText(self.current_profile.username)
        self.password_field.setText(self.current_profile.password)
        self.ssl_checkbox.setChecked(self.current_profile.ssl == 'True')

    def save_settings(self):  # TODO: check if it can be better
        self.current_profile.name = self.name_field.text()
        self.current_profile.host = self.host_field.text()
        self.current_profile.port = self.port_field.text()
        self.current_profile.client_id = self.client_id_field.text()
        self.current_profile.username = self.username_field.text()
        self.current_profile.password = self.password_field.text()
        self.current_profile.ssl = str(self.ssl_checkbox.isChecked())
