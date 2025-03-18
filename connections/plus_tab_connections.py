from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QFontMetrics
from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox

from settings.profile_manager import profile_manager
from UI.interface_utils import create_button
from UI.styles import DELETE_BUTTON
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

mqtt_versions = {
    3: '3.1',
    4: '3.1.1',
    5: '5.0',
}


def parse_mqtt_ver(ver: int):
    if ver == '4':
        return '3.1.1'
    if ver == '3':
        return '3.1'
    if ver == '5':
        return '5.0'


class PlusTabCommon(PlusTabUI):
    def __init__(self):
        super().__init__()
        self._setup_common_connections()

    def _setup_common_connections(self):
        self.ca_folder_button.clicked.connect(
            lambda: self.open_file_dialog(self.ca_field)
        )
        self.client_cert_button.clicked.connect(
            lambda: self.open_file_dialog(self.client_cert_field)
        )
        self.client_key_button.clicked.connect(
            lambda: self.open_file_dialog(self.client_key_field)
        )
        self.self_signed_radio.clicked.connect(lambda: self.set_read_only_certs(False))
        self.ca_signed_radio.clicked.connect(lambda: self.set_read_only_certs(True))
        self.auto_recon_checkbox.stateChanged.connect(self.set_recon_read_only)
        self.auto_recon_checkbox.setChecked(
            profile_manager.current_profile.auto_reconnect
        )
        self.clean_start_checkbox.stateChanged.connect(
            lambda state: self.set_session_expiry_read_only(
                (self.mqtt_ver_field.text() != '5.0') or (state == 2)
            )
        )

        for version in ('3.1.1', '3.1', '5.0'):
            font_metrics = QFontMetrics(self.mqtt_ver_field.font())
            elided_text = font_metrics.elidedText(version, Qt.ElideRight, 110)

            action = QAction(elided_text, self.mqtt_ver_field)
            action.triggered.connect(lambda _, ver=version: self.set_mqtt_ver(ver))
            self.mqtt_ver_menu.addAction(action)

        self.mqtt_ver_field.clicked.connect(self.show_mqtt_ver_menu)

    def set_mqtt_ver(self, ver):
        self.mqtt_ver_field.setText(ver)
        if ver != '5.0':
            tip = 'Only for MQTT 5.0'
            self.set_field_read_only(self.max_packet_field, tip, False)
            self.set_session_expiry_read_only(True)
        else:
            self.set_field_read_only(self.max_packet_field, '', True)
            self.set_session_expiry_read_only(self.clean_start_checkbox.isChecked())

    def set_read_only_certs(self, state: bool):
        for field in (self.ca_field, self.client_cert_field, self.client_key_field):
            self.set_field_read_only(
                field, 'Only for self signed connection', state, contr=True
            )

        for button in (
            self.ca_folder_button,
            self.client_cert_button,
            self.client_key_button,
        ):
            button.setEnabled(not state)

    def set_recon_read_only(self, state):
        tip = 'Only if Auto Reconnect is enabled'
        self.set_field_read_only(self.recon_period_field, tip, state)

    def set_session_expiry_read_only(self, state, debug=None):
        tip = 'Only if MQTT version is 5.0 and clean start is disabled'
        self.set_field_read_only(self.session_expiry_field, tip, state, contr=True)
        return None

    @staticmethod
    def set_field_read_only(field, tooltip, state, contr=False):
        if contr:
            state = not state
        field.setReadOnly(not state)

        if state:
            field.setToolTip('')
            field.setStyleSheet(
                field.styleSheet() + 'QLineEdit {color: rgb(186, 186, 186)}'
            )
        else:
            field.setCursor(QCursor(Qt.ForbiddenCursor))
            field.setToolTip(tooltip)
            field.setStyleSheet(
                field.styleSheet() + 'QLineEdit {color: rgb(120, 120, 120)}'
            )

    def open_file_dialog(self, field):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Choose File', '', 'All Files (*)', options=options
        )
        if file_name:
            field.setText(file_name)


class PlusTab(PlusTabCommon):
    def __init__(self):
        super().__init__()
        self.keep_alive_field.setText('60')
        self.ca_signed_radio.setChecked(True)
        self.set_read_only_certs(True)
        self.auto_recon_checkbox.setChecked(True)
        self.recon_period_field.setText('120')
        self.clean_start_checkbox.setChecked(True)

    def open_file_dialog(self, field):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Choose File', '', 'All Files (*)', options=options
        )
        if file_name:
            field.setText(file_name)

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
            'mqtt_version': self.mqtt_ver_field.text(),
            'connect_timeout': self.con_timeout_field.text(),
            'keep_alive': self.keep_alive_field.text(),
            'auto_reconnect': self.auto_recon_checkbox.isChecked(),
            'reconnect_period': self.recon_period_field.text(),
            'clean_start': self.clean_start_checkbox.isChecked(),
            'session_expiry_interval': self.session_expiry_field.text(),
            'receive_maximum': self.receive_max_field.text(),
            'maximum_packet_size': self.max_packet_field.text(),
            'ca_signed': self.ca_signed_radio.isChecked(),
            'self_signed': self.self_signed_radio.isChecked(),
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
        self.mqtt_ver_field.setText('3.1.1')
        self.con_timeout_field.clear()
        self.keep_alive_field.setText('60')
        self.auto_recon_checkbox.setChecked(False)
        self.recon_period_field.clear()
        self.clean_start_checkbox.setChecked(False)
        self.session_expiry_field.clear()
        self.receive_max_field.clear()
        self.max_packet_field.clear()
        self.setFocus()


class EditTab(PlusTabCommon):
    def __init__(self):
        super().__init__()
        self.delete_button = create_button(
            'Delete',
            self.plus_scroll_layout,
            add_layout=self.plus_scroll_box,
            max_size=[100, 25],
            min_size=[0, 25],
            style=DELETE_BUTTON + 'QPushButton {margin-left: 10px;}',
        )
        self.delete_method = None

        self.setup_connections()
        self.current_profile = profile_manager.current_profile

    def setup_connections(self):
        self.set_read_only_certs(not self.self_signed_radio.isChecked())

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
        self.ssl_checkbox.setChecked(self.current_profile.ssl)
        self.ssl_tls_checkbox.setChecked(self.current_profile.ssl_tls)
        self.ca_signed_radio.setChecked(self.current_profile.ca_signed)
        self.self_signed_radio.setChecked(self.current_profile.self_signed)
        self.ca_field.setText(self.current_profile.ca_file)
        self.client_cert_field.setText(self.current_profile.crt_file)
        self.client_key_field.setText(self.current_profile.key_file)
        self.set_mqtt_ver(mqtt_versions.get(self.current_profile.mqtt_version))
        self.con_timeout_field.setText(self.current_profile.connect_timeout)
        self.keep_alive_field.setText(self.current_profile.keep_alive)
        self.auto_recon_checkbox.setChecked(self.current_profile.auto_reconnect)
        self.set_recon_read_only(self.auto_recon_checkbox.isChecked())
        # self.set_session_expiry_read_only(not all((self.mqtt_ver_field.text() == '5.0', self.clean_start_checkbox.isChecked())))
        self.recon_period_field.setText(self.current_profile.reconnect_period)
        self.clean_start_checkbox.setChecked(self.current_profile.clean_start)
        self.session_expiry_field.setText(self.current_profile.session_expiry_interval)
        self.receive_max_field.setText(self.current_profile.receive_maximum)
        self.max_packet_field.setText(self.current_profile.maximum_packet_size)
        self.set_read_only_certs(not self.self_signed_radio.isChecked())

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
        self.current_profile.ca_file = self.ca_field.text()
        self.current_profile.key_file = self.client_key_field.text()
        self.current_profile.crt_file = self.client_cert_field.text()
        self.current_profile.mqtt_version = self.mqtt_ver_field.text()
        self.current_profile.connect_timeout = self.con_timeout_field.text()
        self.current_profile.keep_alive = self.keep_alive_field.text()
        self.current_profile.auto_reconnect = self.auto_recon_checkbox.isChecked()
        self.current_profile.reconnect_period = self.recon_period_field.text()
        self.current_profile.clean_start = self.clean_start_checkbox.isChecked()
        self.current_profile.session_expiry_interval = self.session_expiry_field.text()
        self.current_profile.receive_maximum = self.receive_max_field.text()
        self.current_profile.maximum_packet_size = self.max_packet_field.text()
