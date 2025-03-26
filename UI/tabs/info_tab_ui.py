import webbrowser

from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QWidget

from UI import styles
from UI.interface_utils import (
    Spacer,
    create_button,
    create_frame,
    create_label,
    create_layout,
    create_spacer,
)


class InfoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.info_layout_grid = QGridLayout(self)
        self.info_layout = QVBoxLayout()
        self.info_frame = create_frame(self)

        self.version_label = create_label('Version 1.0', self.info_frame, align='left')
        font = self.version_label.font()
        font.setPointSize(14)
        font.setBold(True)
        self.version_label.setFont(font)

        self.commercial_label = create_label(
            'This is not commercial project, the creator is considering it as pet project. '
            'Perhaps, you can use it as fully working MQTT Broker.',
            self.info_frame,
            align='left',
        )
        self.hub_label = create_label(
            'MQTT Hub - is a client that can help you to interact with MQTT 5.0, '
            'designed to development to debugging.',
            self.info_frame,
            align='left',
        )

        self.mqttx_info_label = create_label(
            'For reference was taken MQTTX app, check it for the link: mqttx.app',
            self.info_frame,
            align='left',
        )

        self.mqtt_button = create_button(
            'MQTT docs', self.info_frame, [80, 0], [100, 100]
        )
        self.github_button = create_button(
            'GitHub link', self.info_frame, [80, 0], [100, 100], style=styles.APP_BUTTON
        )

        self.git_mqtt_layout = create_layout(QHBoxLayout, spacing=10)
        self.git_mqtt_layout.addWidget(self.github_button)
        self.git_mqtt_layout.addWidget(self.mqtt_button)
        self.git_mqtt_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        self.info_part_main = create_layout(
            QGridLayout, [30, 20, 100, 20], 15, out_layout=self.info_frame
        )
        self.info_part_main.addWidget(self.version_label, 0, 0, 1, 1)
        self.info_part_main.addWidget(self.hub_label, 1, 0, 1, 1)
        self.info_part_main.addWidget(self.commercial_label, 2, 0, 1, 1)
        self.info_part_main.addWidget(self.mqttx_info_label, 3, 0, 1, 1)
        self.info_part_main.addLayout(self.git_mqtt_layout, 5, 0, 1, 1)

        self.info_layout.addWidget(self.info_frame)
        self.info_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.info_layout_grid.addLayout(self.info_layout, 0, 0, 1, 1)

        self.github_button.clicked.connect(
            lambda: webbrowser.open('https://github.com/triukhan/mqtt_hub')
        )
        self.mqtt_button.clicked.connect(lambda: webbrowser.open('https://mqtt.org/'))
