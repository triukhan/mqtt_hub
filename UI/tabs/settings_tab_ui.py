from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QWidget

from UI.interface_utils import (
    Spacer,
    create_field,
    create_folder_field,
    create_frame,
    create_label,
    create_layout,
    create_spacer,
    create_toggle,
)


class SettingsTabUi(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout_10 = create_layout(
            QGridLayout, [12, 10, 12, 5], out_layout=self
        )
        self.settings_layout = create_layout(QVBoxLayout, spacing=10)
        self.logger_label = create_label(
            '  Logger',
            self,
            self.settings_layout,
            min_size=[100, 20],
            max_size=[100, 20],
            align='left',
        )
        self.logger_frame = create_frame(self)
        self.logger_layout = create_layout(
            QGridLayout, [30, 20, 100, 20], 15, out_layout=self.logger_frame
        )

        self.logger_cb_label = create_label(
            'Logger', self.logger_frame, self.logger_layout, [0, 0, 1, 1]
        )
        self.logger_path_label = create_label(
            'Logger Path',
            self.logger_frame,
            self.logger_layout,
            [2, 0, 1, 1],
        )

        self.logger_spin = create_field(
            self.logger_frame,
            self.logger_layout,
            [1, 1, 1, 1],
            spinbox=True,
        )

        self.logger_quantity_label = create_label(
            'Quantity',
            self.logger_frame,
            self.logger_layout,
            [1, 0, 1, 1],
        )

        self.logger_checkbox = create_toggle(self.logger_layout, [0, 1, 1, 1])

        self.logger_path_field, self.logger_path_button = create_folder_field(
            self.logger_frame, self.logger_layout, [2, 1, 1, 1]
        )

        self.settings_layout.addWidget(self.logger_frame)
        self.settings_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.settings_inner_layout = QGridLayout()
        self.settings_layout.addLayout(self.settings_inner_layout)
        self.gridLayout_10.addLayout(self.settings_layout, 0, 0, 1, 1)
