from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QSpinBox, QVBoxLayout, QWidget

from UI import styles
from UI.interface_utils import (
    create_button,
    create_checkbox,
    create_field,
    create_frame,
    create_label,
    create_layout,
    create_spacer, Spacer,
)


class SettingsTabUi(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout_10 = QGridLayout(self)
        self.settings_layout = QVBoxLayout()
        self.logger_label = create_label(
            'Logger',
            self,
            self.settings_layout,
            style=styles.LABEL,
            min_size=[100, 20],
            max_size=[100, 20],
        )
        self.logger_frame = create_frame(self, styles.FRAME_PART)
        self.logger_layout = create_layout(
            QGridLayout, [30, 20, 100, 20], 15, out_layout=self.logger_frame
        )

        self.logger_cb_label = create_label(
            'Logger', self.logger_frame, self.logger_layout, [0, 0, 1, 1], styles.LABEL
        )
        self.logger_path_label = create_label(
            'Logger Path',
            self.logger_frame,
            self.logger_layout,
            [2, 0, 1, 1],
            styles.LABEL,
        )

        self.logger_spin = QSpinBox(self.logger_frame)
        self.logger_spin.setStyleSheet(
            'QSpinBox {color: rgb(186, 189, 182); border: 1px solid rgb(50, 50, 50); background-color: rgb(35, 35, 35);'
            'padding: 5px; border-radius: 5;}'
        )
        self.logger_layout.addWidget(self.logger_spin, 1, 1, 1, 1)

        self.logger_quantity_label = create_label(
            'Quantity',
            self.logger_frame,
            self.logger_layout,
            [1, 0, 1, 1],
            styles.LABEL,
        )

        self.logger_checkbox = create_checkbox(
            self.logger_frame, self.logger_layout, [0, 1, 1, 1]
        )

        self.logger_path_layout = create_layout(QHBoxLayout, spacing=0)
        self.logger_path_field = create_field(
            self.logger_frame, self.logger_path_layout
        )

        self.logger_folder_button = create_button(
            '', self.logger_frame, add_layout=self.logger_path_layout
        )
        self.logger_folder_button.setStyleSheet(
            'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border: 1px solid '
            'rgb(50, 50, 50); border-left: 0px; border-top-right-radius: 5; border-bottom-right-radius: 5;'
            'padding: 6px;}'
        )
        self.logger_layout.addLayout(self.logger_path_layout, 2, 1, 1, 1)

        self.settings_layout.addWidget(self.logger_frame)
        self.settings_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.settings_inner_layout = QGridLayout()
        self.settings_layout.addLayout(self.settings_inner_layout)
        self.gridLayout_10.addLayout(self.settings_layout, 0, 0, 1, 1)
