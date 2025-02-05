from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from GUI import styles
from GUI.interface_utils import (
    create_checkbox,
    create_field,
    create_frame,
    create_label,
    create_radio,
)

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

        # general
        self.general_label = create_label(
            'General',
            self.plus_scroll_layout,
            add_layout=self.plus_scroll_box,
            max_size=(100, 20),
            min_size=(0, 20),
        )

        self.general_frame = create_frame(
            self.plus_scroll_layout, add_layout=self.plus_scroll_box
        )
        self.general_layout = QGridLayout(self.general_frame)  # TODO: custom_func
        self.general_layout.setContentsMargins(30, 20, 60, 20)
        self.general_layout.setSpacing(15)

        self.name_label = create_label(
            'Name', self.general_frame, self.general_layout, [1, 0, 1, 1]
        )
        self.host_label = create_label(
            'Host', self.general_frame, self.general_layout, [2, 0, 1, 1]
        )
        self.port_label = create_label(
            'Port', self.general_frame, self.general_layout, [3, 0, 1, 1]
        )
        self.client_id_label = create_label(
            'Client ID', self.general_frame, self.general_layout, [4, 0, 1, 1]
        )
        self.username_label = create_label(
            'Username', self.general_frame, self.general_layout, [5, 0, 1, 1]
        )
        self.password_label = create_label(
            'Password', self.general_frame, self.general_layout, [6, 0, 1, 1]
        )
        self.ssl_tls_label = create_label(
            'SSL/TLS', self.general_frame, self.general_layout, [7, 0, 1, 1]
        )
        self.ssl_label = create_label(
            'SSL', self.general_frame, self.general_layout, [8, 0, 1, 1]
        )
        self.certificate_label = create_label(
            'Certificate', self.general_frame, self.general_layout, [9, 0, 1, 1]
        )
        self.generate_id_label = create_label(
            'gen', self.general_frame, self.general_layout, [4, 3, 1, 1]
        )
        self.name_info_button = create_label(
            'inf', self.general_frame, self.general_layout, [1, 3, 1, 1]
        )

        self.name_field = create_field(
            self.general_frame, self.general_layout, [1, 2, 1, 1]
        )
        self.host_field = create_field(
            self.general_frame, self.general_layout, [2, 2, 1, 1]
        )
        self.port_field = create_field(
            self.general_frame, self.general_layout, [3, 2, 1, 1]
        )
        self.client_id_field = create_field(
            self.general_frame, self.general_layout, [4, 2, 1, 1]
        )
        self.username_field = create_field(
            self.general_frame, self.general_layout, [5, 2, 1, 1]
        )
        self.password_field = create_field(
            self.general_frame, self.general_layout, [6, 2, 1, 1]
        )

        self.ssl_checkbox = create_checkbox(
            self.general_frame, self.general_layout, [8, 2, 1, 1]
        )
        self.ssl_tls_checkbox = create_checkbox(
            self.general_frame, self.general_layout, [7, 2, 1, 1]
        )

        self.certificate_layout = QHBoxLayout()
        self.ca_signed_radio = create_radio(
            'CA signed server certificate', self.general_frame, self.certificate_layout
        )
        self.self_signed_radio = create_radio(
            'CA or Self signed certificate', self.general_frame, self.certificate_layout
        )
        self.certificate_layout.addItem(vertical_spacer)
        self.general_layout.addLayout(self.certificate_layout, 9, 2, 1, 1)

        # certificates
        self.certificates_label = create_label(
            'Certificates',
            self.plus_scroll_layout,
            self.plus_scroll_box,
            min_size=(100, 30),
            max_size=(100, 30),
        )
        self.certificates_frame = create_frame(self.plus_scroll_layout)

        self.gridLayout_7 = QGridLayout(
            self.certificates_frame
        )  # TODO: custom_func & rename
        self.gridLayout_7.setContentsMargins(30, 20, 100, 20)
        self.gridLayout_7.setSpacing(15)

        self.ca_label = create_label(
            'CA File', self.certificates_frame, self.gridLayout_7, [0, 0, 1, 1]
        )
        self.client_cert_label = create_label(
            'Client Certificate File',
            self.certificates_frame,
            self.gridLayout_7,
            [1, 0, 1, 1],
        )
        self.client_key_label = create_label(
            'Client Key File', self.certificates_frame, self.gridLayout_7, [2, 0, 1, 1]
        )

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

        # advanced
        self.advanced_label = create_label(
            'Advanced',
            self.plus_scroll_layout,
            add_layout=self.plus_scroll_box,
            min_size=(100, 20),
            max_size=(100, 20),
        )

        self.advanced_frame = create_frame(self.plus_scroll_layout)
        self.gridLayout_6 = QGridLayout(
            self.advanced_frame
        )  # TODO: custom_func & rename
        self.gridLayout_6.setContentsMargins(30, -1, 60, 20)
        self.gridLayout_6.setSpacing(15)

        self.con_timeout_label = create_label(
            'Connect Timeout', self.advanced_frame, self.gridLayout_6, [1, 0, 1, 1]
        )
        self.mqtt_ver_label = create_label(
            'MQTT Version', self.advanced_frame, self.gridLayout_6, [0, 0, 1, 1]
        )
        self.keep_alive_label = create_label(
            'Keep Alive', self.advanced_frame, self.gridLayout_6, [2, 0, 1, 1]
        )
        self.auto_reconnect_label = create_label(
            'Auto Reconnect', self.advanced_frame, self.gridLayout_6, [3, 0, 1, 1]
        )
        self.reconnect_period_label = create_label(
            'Reconnect Period', self.advanced_frame, self.gridLayout_6, [4, 0, 1, 1]
        )
        self.clean_start_label = create_label(
            'Clean Start', self.advanced_frame, self.gridLayout_6, [5, 0, 1, 1]
        )
        self.session_expiry_label = create_label(
            'Session Expiry Interval',
            self.advanced_frame,
            self.gridLayout_6,
            [6, 0, 1, 1],
        )
        self.receive_max_label = create_label(
            'Receive Maximum', self.advanced_frame, self.gridLayout_6, [7, 0, 1, 1]
        )
        self.max_packet_label = create_label(
            'Maximum Packet Size', self.advanced_frame, self.gridLayout_6, [8, 0, 1, 1]
        )
        self.topic_alias_label = create_label(
            'Topic Alias Maximum', self.advanced_frame, self.gridLayout_6, [9, 0, 1, 1]
        )
        self.request_resp_label = create_label(
            'Request Response', self.advanced_frame, self.gridLayout_6, [10, 0, 1, 1]
        )
        self.request_problem_label = create_label(
            'Request Problem Info',
            self.advanced_frame,
            self.gridLayout_6,
            [11, 0, 1, 1],
        )
        self.ct_sec_label = create_label(
            'sec', self.advanced_frame, self.gridLayout_6, [1, 4, 1, 1]
        )
        self.ka_sec_label = create_label(
            'sec', self.advanced_frame, self.gridLayout_6, [2, 4, 1, 1]
        )
        self.rp_ms_label = create_label(
            'ms', self.advanced_frame, self.gridLayout_6, [4, 4, 1, 1]
        )
        self.sei_sec_label = create_label(
            'sec', self.advanced_frame, self.gridLayout_6, [6, 4, 1, 1]
        )

        self.con_timeout_field = create_field(
            self.advanced_frame, self.gridLayout_6, [1, 2, 1, 1]
        )
        self.mqtt_ver_field = create_field(
            self.advanced_frame, self.gridLayout_6, [0, 2, 1, 1]
        )
        self.keep_alive_field = create_field(
            self.advanced_frame, self.gridLayout_6, [2, 2, 1, 1]
        )
        self.recon_period_field = create_field(
            self.advanced_frame, self.gridLayout_6, [4, 2, 1, 1]
        )
        self.session_expiry_field = create_field(
            self.advanced_frame, self.gridLayout_6, [6, 2, 1, 1]
        )
        self.receive_max_field = create_field(
            self.advanced_frame, self.gridLayout_6, [7, 2, 1, 1]
        )
        self.max_packet_field = create_field(
            self.advanced_frame, self.gridLayout_6, [8, 2, 1, 1]
        )
        self.topic_alias_field = create_field(
            self.advanced_frame, self.gridLayout_6, [9, 2, 1, 1]
        )

        self.auto_recon_checkbox = create_checkbox(
            self.advanced_frame, self.gridLayout_6, [3, 2, 1, 1]
        )
        self.clean_start_checkbox = create_checkbox(
            self.advanced_frame, self.gridLayout_6, [5, 2, 1, 1]
        )
        self.request_resp_checkbox = create_checkbox(
            self.advanced_frame, self.gridLayout_6, [10, 2, 1, 1]
        )
        self.request_problem_checkbox = create_checkbox(
            self.advanced_frame, self.gridLayout_6, [11, 2, 1, 1]
        )

        self.plus_scroll_box.addWidget(self.advanced_frame)
        self.plus_scroll.setWidget(self.plus_scroll_layout)
        self.plus_layout.addWidget(self.plus_scroll, 0, 1, 1, 1)
