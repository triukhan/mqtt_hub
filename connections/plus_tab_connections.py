from PyQt5.QtWidgets import QMessageBox

from UI.styles import DELETE_BUTTON
from settings.profile_manager import profile_manager
from UI.interface_utils import create_button
from UI.tabs.plus_tab_ui import PlusTabUI

SETTINGS = {
    'name': 'name_field',
    'host': 'host_field',
    'port': 'port_field',
    'client_id': 'client_id_field',
    'username': 'username_field',
    'password': 'password_field',
    'ssl_tls': 'ssl_tls_checkbox',
    'ssl': 'ssl_checkbox',
    'ca_file': 'ca_field',
    'crt_file': 'client_cert_field',
    'key_file': 'client_key_field',
}

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
        self.delete_button = create_button(
            'Delete',
            self.plus_scroll_layout,
            add_layout=self.plus_scroll_box,
            max_size=[100, 25],
            min_size=[0, 25],
            style=DELETE_BUTTON
        )
        self.delete_method = None

        self.setup_connections()
        self.current_profile = profile_manager.current_profile
        self.load_current_profile_settings()

    def setup_connections(self):
        self.client_cert_button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        QMessageBox.information(self, "Info", "Button clicked in Plus Tab!")

    def _update_current_profile(self):
        self.current_profile = profile_manager.current_profile

    def load_current_profile_settings(self):
        self._update_current_profile()
        self.name_field.setText(self.current_profile.name)
        self.host_field.setText(self.current_profile.host)
        self.port_field.setText(self.current_profile.port)
        self.client_id_field.setText(self.current_profile.client_id)
        self.username_field.setText(self.current_profile.username)
        self.password_field.setText(self.current_profile.password)
        self.ssl_checkbox.setChecked(self.current_profile.ssl == 'True')
        self.ssl_tls_checkbox.setChecked(self.current_profile.ssl_tls == 'True')
        self.ca_signed_radio.setChecked(self.current_profile.ca_signed == 'True')
        self.self_signed_radio.setChecked(self.current_profile.self_signed == 'True')
        self.mqtt_ver_field.setText(self.current_profile.mqtt_version)
        self.con_timeout_field.setText(self.current_profile.connect_timeout)
        self.keep_alive_field.setText(self.current_profile.keep_alive)
        self.auto_recon_checkbox.setChecked(self.current_profile.auto_reconnect == 'True')
        self.recon_period_field.setText(self.current_profile.reconnect_period)
        self.clean_start_checkbox.setChecked(self.current_profile.clean_start == 'True')
        self.session_expiry_field.setText(self.current_profile.session_expiry_interval)
        self.receive_max_field.setText(self.current_profile.receive_maximum)
        self.max_packet_field.setText(self.current_profile.maximum_packet_size)
        self.topic_alias_field.setText(self.current_profile.topic_alias_maximum)
        self.request_resp_checkbox.setChecked(self.current_profile.request_response == 'True')
        self.request_problem_checkbox.setChecked(self.current_profile.request_problem_info == 'True')

    def save_settings(self):  # TODO: make dict and set by dict
        self._update_current_profile()
        self.current_profile.name = self.name_field.text()
        self.current_profile.host = self.host_field.text()
        self.current_profile.port = self.port_field.text()
        self.current_profile.client_id = self.client_id_field.text()
        self.current_profile.username = self.username_field.text()
        self.current_profile.password = self.password_field.text()
        self.current_profile.ssl = str(self.ssl_checkbox.isChecked())
        self.current_profile.ssl_tls = str(self.ssl_checkbox.isChecked())
        self.current_profile.ca_signed = self.ca_signed_radio.isChecked()
        self.current_profile.self_signed = self.self_signed_radio.isChecked()
        self.current_profile.mqtt_version = self.mqtt_ver_field.text()
        self.current_profile.connect_timeout = self.con_timeout_field.text()
        self.current_profile.keep_alive = self.keep_alive_field.text()
        self.current_profile.auto_reconnect = self.auto_recon_checkbox.isChecked()
        self.current_profile.reconnect_period = self.recon_period_field.text()
        self.current_profile.clean_start = self.clean_start_checkbox.isChecked()
        self.current_profile.session_expiry_interval = self.session_expiry_field.text()
        self.current_profile.receive_maximum = self.receive_max_field.text()
        self.current_profile.maximum_packet_size = self.max_packet_field.text()
        self.current_profile.topic_alias_maximum = self.topic_alias_field.text()
        self.current_profile.request_response = self.request_resp_checkbox.isChecked()
        self.current_profile.request_problem_info = self.request_problem_checkbox.isChecked()
