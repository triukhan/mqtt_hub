from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)


class MainTab(QWidget):
    def __init__(self):
        super().__init__()
        self.main_tab_layout = QGridLayout(self.main_tab)
        self.main_tab_layout.setContentsMargins(0, 0, 0, 0)
        self.main_tab_layout.setSpacing(0)

        self.main_right_layout = QVBoxLayout()
        self.main_right_layout.setContentsMargins(0, -1, 0, 0)
        self.main_right_layout.setSpacing(0)

        self.clear_frame = QFrame(self.main_tab)
        self.clear_frame.setStyleSheet("QFrame{background-color: rgb(35, 35, 35);}")
        self.clear_layout = QHBoxLayout(self.clear_frame)
        self.clear_layout.setContentsMargins(-1, 15, 10, 19)
        self.clear_layout.setSpacing(0)
        self.clear_layout.addItem(spacer_item)
        self.clear_button = QPushButton(self.clear_frame)
