from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout

from UI.interface_utils import create_button, create_frame, create_label, create_layout
from UI.styles import HEADER_FRAME, WIDGET


class ConfirmationDialogUI(QDialog):
    def __init__(self, parent, text, method):
        super().__init__(parent)
        self._method = method
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.text = text
        self._setup_ui()

    def _setup_ui(self):
        self.setGeometry(350, 300, 400, 300)
        self.resize(350, 200)
        self.setStyleSheet(WIDGET)

        self.main_layout = create_layout(QVBoxLayout, 0, 0, self)
        self.main_frame = create_frame(self, False)
        self.main_layout.addWidget(self.main_frame)
        self.inner_layout = create_layout(QVBoxLayout, 10, 10, self.main_frame)

        self.header_frame = create_frame(self.main_frame, HEADER_FRAME)
        self.header_layout = create_layout(QHBoxLayout, 0, 0, self.header_frame)

        self.header_label = create_label(
            "Confirmation dialog",
            self.header_frame,
            self.header_layout,
            min_size=[0, 30],
            max_size=[16777215, 30],
        )

        self.exit_button = create_button(
            "✕",
            self.header_frame,
            min_size=30,
            max_size=30,
            add_layout=self.header_layout,
        )
        self.exit_button.clicked.connect(self.close)

        self.header_layout.addStretch()
        self.header_layout.addWidget(self.exit_button)

        self.inner_layout.addWidget(self.header_frame)

        self.message_label = create_label(
            self.text,
            self.main_frame,
            self.inner_layout,
            min_size=[0, 50],
            max_size=[16777215, 50],
            align='center',
        )

        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()

        self.cancel_button = create_button(
            "Cancel", self.main_frame, min_size=[50, 30], max_size=[100, 30]
        )
        self.cancel_button.clicked.connect(self.close)

        self.delete_button = create_button(
            "Delete", self.main_frame, min_size=[50, 30], max_size=[100, 30]
        )
        self.delete_button.clicked.connect(self._method_and_close)

        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addSpacing(20)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addStretch()

        self.inner_layout.addLayout(self.button_layout)
        self.inner_layout.addStretch()

    def _method_and_close(self):
        self._method()
        self.close()
