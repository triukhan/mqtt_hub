from PyQt5.QtWidgets import QMessageBox

from GUI.tabs.plus_tab_gui import PlusTabUI
from settings.profile_manager import profile_manager


class PlusTab(PlusTabUI):
    def __init__(self):
        super().__init__()

    def get_settings(self):
        settings = {
            'name': self.name_field.text(),
            'host': self.host_field.text(),
            'port': self.port_field.text(),
            'client_id': self.client_id_field.text(),
            'username': self.username_field.text(),
            'password': self.password_field.text(),
            'ssl_tls': self.ssl_tls_checkbox.isChecked(),
            'ssl': self.ssl_checkbox.isChecked(),
            'ca_file': self.ca_field.text(),
            'crt_file': self.client_cert_field.text(),
            'key_file': self.client_key_field.text(),
        }
        self.clear_settings()
        return settings

    def clear_settings(self):
        self.name_field.clear()
        self.host_field.clear()
        self.port_field.clear()
        self.client_id_field.clear()
        self.username_field.clear()
        self.password_field.clear()
        self.ssl_tls_checkbox.setChecked(False)
        self.ssl_checkbox.setChecked(False)
        self.ca_field.clear()
        self.client_cert_field.clear()
        self.client_key_field.clear()
        self.setFocus()


class EditTab(PlusTabUI):
    def __init__(self):
        super().__init__()
        self.setup_connections()
        self.current_profile = profile_manager.current_profile
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
