from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)

from UI.interface_utils import (
    create_button,
    create_field,
    create_frame,
    create_label,
    create_layout, create_text_edit, create_spacer, Spacer,
)
from UI.styles import DELETE_BUTTON, X_BUTTON


class ClipboardDialogUI:
    def _setup_ui(self, clipboard_dialog, with_delete):
        clipboard_dialog.resize(365, 190)
        clipboard_dialog.setWindowFlags(
            QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint
        )
        clipboard_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        clipboard_dialog.setStyleSheet('background-color: rgba(35, 35, 35, 230);')

        self.main_layout = create_layout(QGridLayout, 0, 0, clipboard_dialog)

        self.main_frame = create_frame(clipboard_dialog)
        self.main_vertical_layout = create_layout(QVBoxLayout, 0, 0, self.main_frame)
        self.header_frame = create_frame(self.main_frame, 'QFrame {border: none;}')
        self.header_layout = create_layout(
            QHBoxLayout, [40, 0, 0, 0], 15, self.header_frame
        )

        left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(left_spacer)
        self.clipboard_label = create_label(
            'Add to Clipboard',
            self.header_frame,
            self.header_layout,
            min_size=[30, 30],
            max_size=[200, 30],
        )

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem)

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
        self.clipboard_layout = create_layout(QVBoxLayout, [20, 20, 20, 10], 10)
        self.name_label = create_label(
            'Enter a name for the Clipboard Message',
            self.main_frame,
            self.clipboard_layout,
            min_size=[0, 30],
            max_size=[1000, 30],
            align='left',
        )
        self.name_field = create_field(self.main_frame, self.clipboard_layout)
        self.body_layout.addLayout(self.clipboard_layout)
        self.text_layout = create_layout(QVBoxLayout, [20, 0, 20, 10], 10)
        self.text_label = create_label(
            'Text',
            self.main_frame,
            self.text_layout,
            min_size=[0, 30],
            max_size=[1000, 30],
            align='left',
        )
        self.text_field = create_text_edit(self.main_frame, 250, add_layout=self.text_layout)

        self.body_layout.addLayout(self.text_layout)

        self.save_layout = create_layout(QHBoxLayout, [20, 15, 20, 15], 10)
        if with_delete:
            self.delete_button = create_button(
                'Delete',
                self.main_frame,
                add_layout=self.save_layout,
                style=DELETE_BUTTON,
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

        QtCore.QMetaObject.connectSlotsByName(clipboard_dialog)
