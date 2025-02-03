from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QCheckBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from GUI import styles

vertical_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
horizontal_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
LABEL_ALIGNMENT = (
    QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
)


class PlusTab(QWidget):
    def __init__(self):
        super().__init__()
        self.plus_layout = QGridLayout(self)
        self.plus_layout.setContentsMargins(0, 0, 0, 0)
        self.plus_layout.setSpacing(0)
        self.plus_scroll = QScrollArea(self)
        self.plus_scroll.setStyleSheet("QScrollArea {border: 0px}")

        self.plus_scroll_layout = QWidget()
        self.plus_scroll_layout.setGeometry(QtCore.QRect(0, 0, 969, 1231))
        self.plus_scroll_box = QVBoxLayout(self.plus_scroll_layout)

        self.general_label = QLabel(self.plus_scroll_layout)
        self.general_label.setText('General')
        self.general_label.setMinimumSize(QtCore.QSize(0, 20))
        self.general_label.setMaximumSize(QtCore.QSize(100, 20))
        self.general_label.setStyleSheet(styles.LABEL)
        self.plus_scroll_box.addWidget(self.general_label)

        self.general_frame = QFrame(self.plus_scroll_layout)
        self.general_frame.setStyleSheet(styles.FRAME_PART)
        self.general_frame.setFrameShape(QFrame.StyledPanel)
        self.general_frame.setFrameShadow(QFrame.Raised)

        self.general_layout = QGridLayout(self.general_frame)
        self.general_layout.setContentsMargins(30, 20, 60, 20)
        self.general_layout.setSpacing(15)

        self.name_label = QLabel(self.general_frame)
        self.name_label.setText('Name')
        self.name_label.setStyleSheet(styles.LABEL)
        self.name_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.name_label, 1, 0, 1, 1)

        self.ssl_tls_label = QLabel(self.general_frame)
        self.ssl_tls_label.setText('SSL/TLS')
        self.ssl_tls_label.setStyleSheet(styles.LABEL)
        self.ssl_tls_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.ssl_tls_label, 7, 0, 1, 1)

        self.port_label = QLabel(self.general_frame)
        self.port_label.setText('Port')
        self.port_label.setStyleSheet(styles.LABEL)
        self.port_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.port_label, 3, 0, 1, 1)

        self.username_field = QLineEdit(self.general_frame)
        self.username_field.setStyleSheet(styles.FIELD)
        self.general_layout.addWidget(self.username_field, 5, 2, 1, 1)

        self.client_id_label = QLabel(self.general_frame)
        self.client_id_label.setText('Client ID')
        self.client_id_label.setStyleSheet(styles.LABEL)
        self.client_id_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.client_id_label, 4, 0, 1, 1)

        self.username_label = QLabel(self.general_frame)
        self.username_label.setText('Username')
        self.username_label.setStyleSheet(styles.LABEL)
        self.username_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.username_label, 5, 0, 1, 1)

        self.generate_id_button = QLabel(self.general_frame)
        self.generate_id_button.setText('gen')
        self.generate_id_button.setStyleSheet(styles.LABEL)
        self.general_layout.addWidget(self.generate_id_button, 4, 3, 1, 1)

        self.name_info_button = QLabel(self.general_frame)
        self.name_info_button.setText('inf')
        self.name_info_button.setStyleSheet(styles.LABEL)
        self.general_layout.addWidget(self.name_info_button, 1, 3, 1, 1)

        self.certificate_label = QLabel(self.general_frame)
        self.certificate_label.setText('Certificate')
        self.certificate_label.setStyleSheet(styles.LABEL)
        self.certificate_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.certificate_label, 9, 0, 1, 1)

        self.ssl_label = QLabel(self.general_frame)
        self.ssl_label.setText('SSL')
        self.ssl_label.setStyleSheet(styles.LABEL)
        self.ssl_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.ssl_label, 8, 0, 1, 1)

        self.ssl_checkbox = QCheckBox(self.general_frame)
        self.ssl_checkbox.setStyleSheet(styles.CHECK_BOX)
        self.ssl_checkbox.setText('')
        self.general_layout.addWidget(self.ssl_checkbox, 8, 2, 1, 1)

        self.name_field = QLineEdit(self.general_frame)
        self.name_field.setStyleSheet(styles.FIELD)
        self.general_layout.addWidget(self.name_field, 1, 2, 1, 1)

        self.port_field = QLineEdit(self.general_frame)
        self.port_field.setStyleSheet(styles.FIELD)
        self.general_layout.addWidget(self.port_field, 3, 2, 1, 1)

        self.host_field = QLineEdit(self.general_frame)
        self.host_field.setStyleSheet(styles.FIELD)
        self.general_layout.addWidget(self.host_field, 2, 2, 1, 1)

        self.host_label = QLabel(self.general_frame)
        self.host_label.setText('Host')
        self.host_label.setStyleSheet(styles.LABEL)
        self.host_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.host_label, 2, 0, 1, 1)

        self.password_label = QLabel(self.general_frame)
        self.password_label.setText('Password')
        self.password_label.setStyleSheet(styles.LABEL)
        self.password_label.setAlignment(LABEL_ALIGNMENT)
        self.general_layout.addWidget(self.password_label, 6, 0, 1, 1)

        self.ssl_tls_checkbox = QCheckBox(self.general_frame)
        self.ssl_tls_checkbox.setStyleSheet(styles.CHECK_BOX)
        self.ssl_tls_checkbox.setText('')
        self.general_layout.addWidget(self.ssl_tls_checkbox, 7, 2, 1, 1)

        self.client_id_field = QLineEdit(self.general_frame)
        self.client_id_field.setStyleSheet(styles.FIELD)
        self.general_layout.addWidget(self.client_id_field, 4, 2, 1, 1)

        self.password_field = QLineEdit(self.general_frame)
        self.password_field.setStyleSheet(styles.FIELD)
        self.general_layout.addWidget(self.password_field, 6, 2, 1, 1)

        self.certificate_layout = QHBoxLayout()

        self.ca_signed_radio = QRadioButton(self.general_frame)
        self.ca_signed_radio.setText('CA signed server certificate')
        self.ca_signed_radio.setStyleSheet(styles.RADIO)
        self.certificate_layout.addWidget(self.ca_signed_radio)

        self.self_signed_radio = QRadioButton(self.general_frame)
        self.self_signed_radio.setText('CA or Self signed certificate')
        self.self_signed_radio.setStyleSheet(styles.RADIO)
        self.certificate_layout.addWidget(self.self_signed_radio)

        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.certificate_layout.addItem(spacerItem2)
        self.general_layout.addLayout(self.certificate_layout, 9, 2, 1, 1)
        self.plus_scroll_box.addWidget(self.general_frame)

        self.certificates_label = QLabel(self.plus_scroll_layout)
        self.certificates_label.setText('Certificates')
        self.certificates_label.setMinimumSize(QtCore.QSize(100, 30))
        self.certificates_label.setMaximumSize(QtCore.QSize(100, 30))
        self.certificates_label.setStyleSheet(styles.LABEL)
        self.plus_scroll_box.addWidget(self.certificates_label)

        self.certificates_frame = QFrame(self.plus_scroll_layout)
        self.certificates_frame.setStyleSheet(styles.FRAME_PART)

        self.gridLayout_7 = QGridLayout(self.certificates_frame)
        self.gridLayout_7.setContentsMargins(30, 20, 100, 20)
        self.gridLayout_7.setSpacing(15)

        self.ca_label = QLabel(self.certificates_frame)
        self.ca_label.setText('CA File')
        self.ca_label.setStyleSheet(styles.LABEL)
        self.ca_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_7.addWidget(self.ca_label, 0, 0, 1, 1)

        self.client_cert_label = QLabel(self.certificates_frame)
        self.client_cert_label.setText('Client Certificate File')
        self.client_cert_label.setStyleSheet(styles.LABEL)
        self.client_cert_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_7.addWidget(self.client_cert_label, 1, 0, 1, 1)

        self.client_key_label = QLabel(self.certificates_frame)
        self.client_key_label.setText('Client Key File')
        self.client_key_label.setStyleSheet(styles.LABEL)
        self.client_key_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_7.addWidget(self.client_key_label, 2, 0, 1, 1)

        self.ca_layout = QHBoxLayout()
        self.ca_layout.setSpacing(0)

        self.ca_field = QLineEdit(self.certificates_frame)
        self.ca_field.setStyleSheet(styles.FOLDER_FIELD_LEFT)
        self.ca_layout.addWidget(self.ca_field)

        self.ca_button = QPushButton(self.certificates_frame)
        self.ca_button.setText('fff')
        self.ca_button.setStyleSheet(styles.FOLDER_FIELD_RIGHT)
        self.ca_layout.addWidget(self.ca_button)

        self.gridLayout_7.addLayout(self.ca_layout, 0, 1, 1, 1)

        self.client_cert_layout = QHBoxLayout()
        self.client_cert_layout.setSpacing(0)
        self.client_cert_field = QLineEdit(self.certificates_frame)
        self.client_cert_field.setStyleSheet(styles.FOLDER_FIELD_LEFT)
        self.client_cert_layout.addWidget(self.client_cert_field)

        self.client_cert_button = QPushButton(self.certificates_frame)
        self.client_cert_button.setText('fff')
        self.client_cert_button.setStyleSheet(styles.FOLDER_FIELD_RIGHT)
        self.client_cert_layout.addWidget(self.client_cert_button)
        self.gridLayout_7.addLayout(self.client_cert_layout, 1, 1, 1, 1)

        self.client_key_layout = QHBoxLayout()
        self.client_key_layout.setSpacing(0)
        self.client_key_field = QLineEdit(self.certificates_frame)
        self.client_key_field.setStyleSheet(styles.FOLDER_FIELD_LEFT)
        self.client_key_layout.addWidget(self.client_key_field)

        self.client_key_button = QPushButton(self.certificates_frame)
        self.client_key_button.setText('fff')
        self.client_key_button.setStyleSheet(styles.FOLDER_FIELD_RIGHT)
        self.client_key_layout.addWidget(self.client_key_button)

        self.gridLayout_7.addLayout(self.client_key_layout, 2, 1, 1, 1)
        self.plus_scroll_box.addWidget(self.certificates_frame)

        self.advanced_label = QLabel(self.plus_scroll_layout)
        self.advanced_label.setText('Advanced')
        self.advanced_label.setMinimumSize(QtCore.QSize(100, 20))
        self.advanced_label.setMaximumSize(QtCore.QSize(100, 20))
        self.advanced_label.setStyleSheet(styles.LABEL)
        self.plus_scroll_box.addWidget(self.advanced_label)

        self.advanced_frame = QFrame(self.plus_scroll_layout)
        self.advanced_frame.setStyleSheet(styles.FRAME_PART)
        self.advanced_frame.setFrameShape(QFrame.StyledPanel)
        self.advanced_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_6 = QGridLayout(self.advanced_frame)
        self.gridLayout_6.setContentsMargins(30, -1, 60, 20)
        self.gridLayout_6.setSpacing(15)

        self.keep_alive_field = QLineEdit(self.advanced_frame)
        self.keep_alive_field.setStyleSheet(styles.FIELD)
        self.gridLayout_6.addWidget(self.keep_alive_field, 2, 2, 1, 1)

        self.auto_reconnect_label = QLabel(self.advanced_frame)
        self.auto_reconnect_label.setText('Auto Reconnect')
        self.auto_reconnect_label.setStyleSheet(styles.LABEL)
        self.auto_reconnect_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.auto_reconnect_label, 3, 0, 1, 1)

        self.clean_start_checkbox = QCheckBox(self.advanced_frame)
        self.clean_start_checkbox.setStyleSheet(styles.CHECK_BOX)
        self.clean_start_checkbox.setText("")
        self.gridLayout_6.addWidget(self.clean_start_checkbox, 5, 2, 1, 1)

        self.session_expiry_label_2 = QLineEdit(self.advanced_frame)
        self.session_expiry_label_2.setStyleSheet(styles.LABEL)
        self.gridLayout_6.addWidget(self.session_expiry_label_2, 6, 2, 1, 1)

        self.request_resp_checkbox = QCheckBox(self.advanced_frame)
        self.request_resp_checkbox.setStyleSheet(styles.CHECK_BOX)
        self.request_resp_checkbox.setText("")
        self.gridLayout_6.addWidget(self.request_resp_checkbox, 10, 2, 1, 1)

        self.max_packet_field = QLineEdit(self.advanced_frame)
        self.max_packet_field.setStyleSheet(styles.FIELD)
        self.gridLayout_6.addWidget(self.max_packet_field, 8, 2, 1, 1)

        self.request_problem_checkbox = QCheckBox(self.advanced_frame)
        self.request_problem_checkbox.setStyleSheet(styles.CHECK_BOX)
        self.request_problem_checkbox.setText("")
        self.gridLayout_6.addWidget(self.request_problem_checkbox, 11, 2, 1, 1)

        self.recon_period_label = QLineEdit(self.advanced_frame)
        self.recon_period_label.setStyleSheet(styles.LABEL)
        self.gridLayout_6.addWidget(self.recon_period_label, 4, 2, 1, 1)

        self.topic_alias_field = QLineEdit(self.advanced_frame)
        self.topic_alias_field.setStyleSheet(styles.FIELD)
        self.gridLayout_6.addWidget(self.topic_alias_field, 9, 2, 1, 1)

        self.rp_ms_label = QLabel(self.advanced_frame)
        self.rp_ms_label.setText('ms')
        self.rp_ms_label.setStyleSheet(styles.LABEL)
        self.gridLayout_6.addWidget(self.rp_ms_label, 4, 4, 1, 1)

        self.sei_sec_label = QLabel(self.advanced_frame)
        self.sei_sec_label.setText('sec')
        self.sei_sec_label.setStyleSheet(styles.LABEL)
        self.gridLayout_6.addWidget(self.sei_sec_label, 6, 4, 1, 1)

        self.ka_sec_label = QLabel(self.advanced_frame)
        self.ka_sec_label.setText('sec')
        self.ka_sec_label.setStyleSheet(styles.LABEL)
        self.ka_sec_label.setObjectName("ka_sec_label")
        self.gridLayout_6.addWidget(self.ka_sec_label, 2, 4, 1, 1)

        self.max_packet_label = QLabel(self.advanced_frame)
        self.max_packet_label.setText('Maximum Packet Size')
        self.max_packet_label.setStyleSheet(styles.LABEL)
        self.max_packet_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.max_packet_label, 8, 0, 1, 1)

        self.topic_alias_label = QLabel(self.advanced_frame)
        self.topic_alias_label.setText('Topic Alias Maximum')
        self.topic_alias_label.setStyleSheet(styles.LABEL)
        self.topic_alias_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.topic_alias_label, 9, 0, 1, 1)

        self.keep_alive_label = QLabel(self.advanced_frame)
        self.keep_alive_label.setText('Keep Alive')
        self.keep_alive_label.setStyleSheet(styles.LABEL)
        self.keep_alive_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.keep_alive_label, 2, 0, 1, 1)

        self.mqtt_ver_field = QLineEdit(self.advanced_frame)
        self.mqtt_ver_field.setStyleSheet(styles.FIELD)
        self.gridLayout_6.addWidget(self.mqtt_ver_field, 0, 2, 1, 1)

        self.clean_start_label = QLabel(self.advanced_frame)
        self.clean_start_label.setText('Clean Start')
        self.clean_start_label.setStyleSheet(styles.LABEL)
        self.clean_start_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.clean_start_label, 5, 0, 1, 1)

        self.session_expiry_label = QLabel(self.advanced_frame)
        self.session_expiry_label.setText('Session Expiry Interval')
        self.session_expiry_label.setStyleSheet(styles.LABEL)
        self.session_expiry_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.session_expiry_label, 6, 0, 1, 1)

        self.con_timeout_label = QLabel(self.advanced_frame)
        self.con_timeout_label.setText('Connect Timeout')
        self.con_timeout_label.setStyleSheet(styles.LABEL)
        self.con_timeout_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.con_timeout_label, 1, 0, 1, 1)

        self.mqtt_ver_label = QLabel(self.advanced_frame)
        self.mqtt_ver_label.setText('MQTT Version')
        self.mqtt_ver_label.setStyleSheet(styles.LABEL)
        self.mqtt_ver_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.mqtt_ver_label, 0, 0, 1, 1)

        self.request_resp_label = QLabel(self.advanced_frame)
        self.request_resp_label.setText('Request Response')
        self.request_resp_label.setStyleSheet(styles.LABEL)
        self.request_resp_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.request_resp_label, 10, 0, 1, 1)

        self.auto_recon_checkbox = QCheckBox(self.advanced_frame)
        self.auto_recon_checkbox.setStyleSheet(styles.CHECK_BOX)
        self.auto_recon_checkbox.setText("")
        self.gridLayout_6.addWidget(self.auto_recon_checkbox, 3, 2, 1, 1)

        self.reconnect_period_label = QLabel(self.advanced_frame)
        self.reconnect_period_label.setText('Reconnect Period')
        self.reconnect_period_label.setStyleSheet(styles.LABEL)
        self.reconnect_period_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.reconnect_period_label, 4, 0, 1, 1)

        self.receive_max_field = QLineEdit(self.advanced_frame)
        self.receive_max_field.setStyleSheet(styles.FIELD)
        self.gridLayout_6.addWidget(self.receive_max_field, 7, 2, 1, 1)

        self.request_problem_label = QLabel(self.advanced_frame)
        self.request_problem_label.setText('Request Problem Info')
        self.request_problem_label.setStyleSheet(styles.LABEL)
        self.request_problem_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.request_problem_label, 11, 0, 1, 1)

        self.receive_max_label = QLabel(self.advanced_frame)
        self.receive_max_label.setText('Receive Maximum')
        self.receive_max_label.setStyleSheet(styles.LABEL)
        self.receive_max_label.setAlignment(LABEL_ALIGNMENT)
        self.gridLayout_6.addWidget(self.receive_max_label, 7, 0, 1, 1)

        self.con_timeout_field = QLineEdit(self.advanced_frame)
        self.con_timeout_field.setStyleSheet(styles.FIELD)
        self.gridLayout_6.addWidget(self.con_timeout_field, 1, 2, 1, 1)

        self.ct_sec_label = QLabel(self.advanced_frame)
        self.ct_sec_label.setText('sec')
        self.ct_sec_label.setStyleSheet(styles.LABEL)
        self.gridLayout_6.addWidget(self.ct_sec_label, 1, 4, 1, 1)

        self.plus_scroll_box.addWidget(self.advanced_frame)
        self.plus_scroll.setWidget(self.plus_scroll_layout)
        self.plus_layout.addWidget(self.plus_scroll, 0, 1, 1, 1)
