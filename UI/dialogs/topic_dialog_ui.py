from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout

from UI.interface_utils import (
    Spacer,
    create_button,
    create_checkbox,
    create_field,
    create_frame,
    create_label,
    create_layout,
    create_spacer,
)
from UI.styles import HEADER_FRAME, WIDGET


class TopicDialogUI:
    def _setup_ui(self, dialog):
        self.dialog = dialog
        self.dialog.resize(530, 530)
        self.dialog.setStyleSheet(WIDGET)

        self.main_layout = create_layout(QGridLayout, 0, 0, self.dialog)
        self.main_frame = create_frame(self.dialog, False)
        self.main_vertical_layout = create_layout(QVBoxLayout, 0, 0, self.main_frame)

        self.header_frame = create_frame(self.main_frame, HEADER_FRAME)
        self.header_frame.setFixedHeight(40)

        self.header_layout = create_layout(
            QHBoxLayout, [15, 0, 0, 0], 15, self.header_frame
        )
        self.header_label = create_label(
            'Edit Topic',
            self.header_frame,
            self.header_layout,
            min_size=[30, 30],
            max_size=[200, 30],
        )
        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.exit_button = create_button(
            'x',
            self.header_frame,
            min_size=30,
            max_size=30,
            add_layout=self.header_layout,
        )
        self.main_vertical_layout.addWidget(self.header_frame)

        self.body_layout = create_layout(QVBoxLayout, spacing=0)

        self.topic_layout = create_layout(QVBoxLayout, [20, 10, 20, 10], 10)
        self.topic_label = create_label(
            'Topic',
            self.main_frame,
            self.topic_layout,
            min_size=[0, 30],
            max_size=[16777215, 30],
        )
        self.topic_field = create_field(self.main_frame, self.topic_layout)
        self.body_layout.addLayout(self.topic_layout)

        self.alias_layout = create_layout(QVBoxLayout, [20, 0, 20, 5], 10)
        self.alias_label = create_label(
            'Alias',
            self.main_frame,
            self.alias_layout,
            min_size=[0, 35],
            max_size=[16777215, 30],
        )
        self.alias_field = create_field(self.main_frame, self.alias_layout)
        self.body_layout.addLayout(self.alias_layout)

        self.qos_color_layout = create_layout(QGridLayout, [20, 15, 20, 15])
        self.qos_color_layout.setHorizontalSpacing(20)
        self.qos_color_layout.setVerticalSpacing(15)
        self.qos_field = create_field(
            self.main_frame, self.qos_color_layout, [1, 0, 1, 1]
        )
        self.qos_field.setMinimumSize(QtCore.QSize(230, 30))
        self.qos_field.setMaximumSize(QtCore.QSize(200, 30))
        self.qos_label = create_label(
            'Qos', self.main_frame, self.qos_color_layout, [0, 0, 1, 1]
        )
        self.color_layout = create_layout(QHBoxLayout)
        self.color_label = create_label('Color', self.main_frame, self.color_layout)
        self.color_button = create_button(
            '■', self.main_frame, min_size=30, max_size=30, add_layout=self.color_layout
        )
        self.qos_color_layout.addLayout(self.color_layout, 0, 3, 1, 1)
        self.color_field = create_field(
            self.main_frame, self.qos_color_layout, [1, 3, 1, 1]
        )
        self.color_field.setMinimumSize(QtCore.QSize(230, 30))
        self.color_field.setMaximumSize(QtCore.QSize(200, 30))
        self.body_layout.addLayout(self.qos_color_layout)

        self.no_local_layout = create_layout(QHBoxLayout, [20, 15, 20, 15])
        self.no_local_label = create_label(
            'No Local Flag', self.main_frame, self.no_local_layout
        )
        self.no_local_checkbox = create_checkbox(self.main_frame, self.no_local_layout)
        self.body_layout.addLayout(self.no_local_layout)

        self.retain_published_layout = create_layout(QHBoxLayout, [20, 15, 20, 15])
        self.retain_published_label = create_label(
            'Retain as Published Flag', self.main_frame, self.retain_published_layout
        )
        self.retain_published_checkbox = create_checkbox(
            self.main_frame, self.retain_published_layout
        )
        self.body_layout.addLayout(self.retain_published_layout)

        self.retain_handling_layout = create_layout(QHBoxLayout, [20, 15, 20, 15], 15)
        self.retain_handling_label = create_label(
            'Retain Handling', self.main_frame, self.retain_handling_layout
        )
        self.retain_handling_field = create_field(
            self.main_frame, self.retain_handling_layout
        )
        self.body_layout.addLayout(self.retain_handling_layout)

        self.save_layout = create_layout(QHBoxLayout, [-1, 15, 20, 15], 15)
        self.delete_button = create_button(
            'Delete', self.main_frame, add_layout=self.save_layout
        )
        self.save_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.cancel_button = create_button(
            'Cancel', self.main_frame, add_layout=self.save_layout
        )
        self.save_button = create_button(
            'Save', self.main_frame, add_layout=self.save_layout
        )
        self.body_layout.addLayout(self.save_layout)

        self.main_vertical_layout.addLayout(self.body_layout)
        self.main_layout.addWidget(self.main_frame, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
