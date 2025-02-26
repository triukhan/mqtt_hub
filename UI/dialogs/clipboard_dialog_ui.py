from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout

from UI.interface_utils import create_button, create_label, create_field, create_layout, create_frame
from UI.styles import X_BUTTON


class ClipboardDialogUI:
    def _setup_ui(self, clipboard_dialog):
        clipboard_dialog.resize(365, 190)
        clipboard_dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
        clipboard_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        clipboard_dialog.setStyleSheet("background-color: rgba(35, 35, 35, 230);")

        self.main_layout = create_layout(QGridLayout, 0, 0, clipboard_dialog)

        self.main_frame = create_frame(clipboard_dialog)
        self.main_vertical_layout = create_layout(QVBoxLayout, 0, 0, self.main_frame)
        self.header_frame = create_frame(self.main_frame)
        self.header_frame.setStyleSheet("QFrame {border: none;}")

        self.header_layout = create_layout(QHBoxLayout, [40, 0, 0, 0], 15, self.header_frame)

        left_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_layout.addItem(left_spacer)
        self.clipboard_label = create_label('Add to Clipboard', self.header_frame, self.header_layout, min_size=(30, 30), max_size=(200, 30))

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.header_layout.addItem(spacerItem)

        self.exit_button = create_button('x', self.header_frame, X_BUTTON, 30, 30, self.header_layout)

        self.main_vertical_layout.addWidget(self.header_frame)

        self.body_layout = create_layout(QVBoxLayout, spacing=0)
        self.clipboard_layout = create_layout(QVBoxLayout, [20, 10, 20, 10], 10)
        self.name_label = create_label('Enter a name for the Clipboard Message', self.main_frame, self.clipboard_layout, min_size=(0, 30), max_size=(1000, 30))
        self.name_field = create_field(self.main_frame, self.clipboard_layout)
        self.body_layout.addLayout(self.clipboard_layout)
        self.text_layout = create_layout(QVBoxLayout, [20, 10, 20, 10], 10)
        self.text_label = create_label('Text', self.main_frame, self.text_layout, min_size=(0, 30), max_size=(1000, 30))
        self.text_field = QTextEdit(self.main_frame)
        self.text_field.setMinimumHeight(250)
        self.text_layout.addWidget(self.text_field)
        self.body_layout.addLayout(self.text_layout)

        self.save_layout = create_layout(QHBoxLayout, [-1, 15, 20, 15], 15)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.save_layout.addItem(spacerItem1)
        self.cancel_button = create_button('Cancel', self.main_frame, add_layout=self.save_layout)
        self.save_button = create_button('Save', self.main_frame, add_layout=self.save_layout)

        self.body_layout.addLayout(self.save_layout)
        self.main_vertical_layout.addLayout(self.body_layout)
        self.main_layout.addWidget(self.main_frame, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(clipboard_dialog)

