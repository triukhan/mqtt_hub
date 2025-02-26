from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from UI import styles
from UI.interface_utils import create_spacer, Spacer


class InfoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.info_layout_grid = QGridLayout(self)
        self.info_layout = QVBoxLayout()
        self.info_frame = QFrame(self)
        self.info_frame.setStyleSheet(
            "QFrame{background-color: rgb(35, 35, 35); border-radius: 5; border: 1px solid rgb(50, 50, 50);}"
        )

        self.version_label = QLabel(self.info_frame)
        self.version_label.setText('Version 1.0')
        self.version_label.setStyleSheet(styles.LABEL)

        self.commercial_label = QLabel(self.info_frame)
        self.commercial_label.setText(
            'This is not commercial project, the creator is considering it as pet project. '
            'Perhaps, you can use it as fully working MQTT Broker.'
        )
        self.commercial_label.setStyleSheet(styles.LABEL)

        self.hub_label = QLabel(self.info_frame)
        self.hub_label.setStyleSheet(styles.LABEL)
        self.hub_label.setText(
            'MQTT Hub - is a client that can help you to interact with MQTT 5.0, '
            'designed to development to debugging.'
        )

        self.mqttx_info_label = QLabel(self.info_frame)
        self.mqttx_info_label.setText(
            'For reference was taken MQTTX app, check it for the link: mqttx.app'
        )
        self.mqttx_info_label.setStyleSheet(styles.LABEL)

        self.mqtt_button = QPushButton(self.info_frame)
        self.mqtt_button.setText('MQTT docs')
        self.mqtt_button.setMinimumSize(QtCore.QSize(80, 0))
        self.mqtt_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.mqtt_button.setStyleSheet(styles.APP_BUTTON)

        self.github_button = QPushButton(self.info_frame)
        self.github_button.setText('GitHub link')
        self.github_button.setMinimumSize(QtCore.QSize(80, 0))
        self.github_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.github_button.setStyleSheet(styles.APP_BUTTON)

        self.git_mqtt_layout = QHBoxLayout()
        self.git_mqtt_layout.addWidget(self.github_button)
        self.git_mqtt_layout.addWidget(self.mqtt_button)
        self.git_mqtt_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        self.info_part_main = QGridLayout(self.info_frame)
        self.info_part_main.setContentsMargins(30, 20, 100, 20)
        self.info_part_main.setSpacing(15)
        self.info_part_main.addWidget(self.version_label, 0, 0, 1, 1)
        self.info_part_main.addWidget(self.hub_label, 1, 0, 1, 1)
        self.info_part_main.addWidget(self.commercial_label, 2, 0, 1, 1)
        self.info_part_main.addWidget(self.mqttx_info_label, 3, 0, 1, 1)
        self.info_part_main.addLayout(self.git_mqtt_layout, 5, 0, 1, 1)

        self.info_layout.addWidget(self.info_frame)
        self.info_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.info_layout_grid.addLayout(self.info_layout, 0, 0, 1, 1)
