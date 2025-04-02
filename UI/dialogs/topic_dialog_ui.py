from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout

from UI.interface_utils import (
    Spacer,
    create_button,
    create_field,
    create_frame,
    create_label,
    create_layout,
    create_spacer,
    create_toggle,
)
from UI.styles import DELETE_BUTTON, LABEL, WIDGET, X_BUTTON


class TopicDialogUI:
    def _setup_ui(self, dialog):
        self.dialog = dialog
        self.dialog.resize(1, 1)
        self.dialog.setStyleSheet(WIDGET)
        self.dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.main_layout = create_layout(QGridLayout, 0, 0, self.dialog)
        self.main_frame = create_frame(self.dialog, False)
        self.main_vertical_layout = create_layout(QVBoxLayout, 0, 0, self.main_frame)

        self.header_frame = create_frame(self.main_frame, 'QFrame {border: none;}')

        self.header_layout = create_layout(
            QHBoxLayout, [15, 0, 0, 10], 15, self.header_frame
        )
        self.header_label = create_label(
            'Edit Topic',
            self.header_frame,
            self.header_layout,
            min_size=[30, 30],
            max_size=[200, 30],
            style=LABEL + 'QLabel {margin-top: 10px;}',
        )

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.exit_button = create_button(
            '✕',
            self.header_frame,
            30,
            30,
            self.header_layout,
            style=X_BUTTON,
            body=True,
            start_value=(35, 35, 35),
        )
        self.main_vertical_layout.addWidget(self.header_frame)

        self.body_layout = create_layout(QVBoxLayout, spacing=0)

        self.topic_layout = create_layout(QVBoxLayout, [20, 10, 20, 5], 5)
        self.topic_label = create_label(
            ' Topic',
            self.main_frame,
            self.topic_layout,
            align='left',
            min_size=[0, 30],
            max_size=[16777215, 30],
        )
        self.topic_field = create_field(self.main_frame, self.topic_layout)
        self.body_layout.addLayout(self.topic_layout)

        self.alias_layout = create_layout(QVBoxLayout, [20, 0, 20, 5], 5)
        self.alias_label = create_label(
            ' Alias',
            self.main_frame,
            self.alias_layout,
            align='left',
            min_size=[0, 35],
            max_size=[16777215, 30],
        )
        self.alias_field = create_field(self.main_frame, self.alias_layout)
        self.body_layout.addLayout(self.alias_layout)

        self.qos_color_layout = create_layout(QGridLayout, [20, 5, 20, 15])
        self.qos_color_layout.setHorizontalSpacing(20)
        self.qos_color_layout.setVerticalSpacing(5)
        self.qos_field = create_field(
            self.main_frame,
            self.qos_color_layout,
            [1, 0, 1, 1],
            spinbox=True,
        )
        self.qos_field.setMaximum(2)

        self.qos_field.setMinimumSize(QtCore.QSize(230, 30))
        self.qos_field.setMaximumSize(QtCore.QSize(200, 30))
        self.qos_label = create_label(
            ' Qos',
            self.main_frame,
            self.qos_color_layout,
            [0, 0, 1, 1],
            align='left',
        )
        self.color_layout = create_layout(QHBoxLayout)
        self.color_label = create_label(
            'Color', self.main_frame, self.color_layout, align='left'
        )
        self.color_button = create_button(
            '■',
            self.main_frame,
            min_size=30,
            max_size=30,
            add_layout=self.color_layout,
            style=LABEL + 'QPushButton {margin-bottom: 2px;}',
        )
        self.qos_color_layout.addLayout(self.color_layout, 0, 3, 1, 1)
        self.color_field = create_field(
            self.main_frame, self.qos_color_layout, [1, 3, 1, 1]
        )
        self.color_field.setMinimumSize(QtCore.QSize(230, 30))
        self.color_field.setMaximumSize(QtCore.QSize(200, 30))
        self.body_layout.addLayout(self.qos_color_layout)

        self.no_local_layout = create_layout(
            QHBoxLayout, [25, 0, 20, 5], align=Qt.AlignLeft
        )
        self.no_local_label = create_label(
            'No Local Flag',
            self.main_frame,
            self.no_local_layout,
            max_size=[190, 30],
            min_size=[190, 30],
            align='left',
        )
        self.no_local_checkbox = create_toggle(self.no_local_layout)
        self.body_layout.addLayout(self.no_local_layout)

        self.retain_published_layout = create_layout(
            QHBoxLayout, [25, 0, 20, 5], align=Qt.AlignLeft
        )
        self.retain_published_label = create_label(
            'Retain as Published Flag',
            self.main_frame,
            self.retain_published_layout,
            max_size=[190, 30],
            min_size=[190, 30],
            align='left',
        )
        self.retain_published_checkbox = create_toggle(self.retain_published_layout)
        self.body_layout.addLayout(self.retain_published_layout)

        self.retain_handling_layout = create_layout(QHBoxLayout, [25, 5, 20, 15], 10)
        self.retain_handling_label = create_label(
            'Retain Handling',
            self.main_frame,
            self.retain_handling_layout,
            align='left',
        )
        self.retain_handling_field = create_field(
            self.main_frame, self.retain_handling_layout, spinbox=True
        )
        self.retain_handling_field.setMinimumSize(QtCore.QSize(360, 30))
        self.retain_handling_field.setMaximum(2)

        self.body_layout.addLayout(self.retain_handling_layout)

        self.save_layout = create_layout(QHBoxLayout, [25, 15, 20, 15], 15)
        self.delete_button = create_button(
            'Delete', self.main_frame, add_layout=self.save_layout, style=DELETE_BUTTON
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
