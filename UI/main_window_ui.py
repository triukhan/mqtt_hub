from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from connections.main_tab_connections import MainTab
from connections.plus_tab_connections import EditTab, PlusTab
from settings.profile_manager import profile_manager
from UI import styles
from UI.interface_utils import (
    Spacer,
    create_button,
    create_frame,
    create_label,
    create_layout,
    create_spacer,
)
from UI.tabs.info_tab_ui import InfoTab
from UI.tabs.settings_tab_ui import SettingsTabUi


class MqttHubUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 50, 1066, 904)
        self.drag_pos = None
        self.main_tab = MainTab()

        self.sidebar_layout = QtWidgets.QVBoxLayout()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None

    def setup_ui(self):
        self.main_window = QtWidgets.QWidget(self)
        self.main_window.setStyleSheet(
            "QWidget {\n" "    background-color: rgb(30, 30, 30);\n" "}\n" ""
        )
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_window)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_w = QtWidgets.QGridLayout()
        self.main_w.setSpacing(0)

        self.tab_layout = QtWidgets.QGridLayout()
        self.tab_layout.setSpacing(0)
        self.all_tabs = QtWidgets.QTabWidget(self.main_window)
        self.all_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.all_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.all_tabs.setElideMode(QtCore.Qt.ElideRight)
        self.all_tabs.setUsesScrollButtons(False)
        self.all_tabs.setTabsClosable(False)
        self.all_tabs.setMovable(False)
        self.all_tabs.setTabBarAutoHide(False)
        self.all_tabs.addTab(self.main_tab, '')
        self.plus_tab = PlusTab()
        self.all_tabs.addTab(self.plus_tab, '')
        self.edit_tab = EditTab()
        self.all_tabs.addTab(self.edit_tab, '')

        self.all_tabs.addTab(SettingsTabUi(), '')
        self.all_tabs.addTab(InfoTab(), '')
        self.tab_layout.addWidget(self.all_tabs, 0, 0, 1, 1)
        self.main_w.addLayout(self.tab_layout, 1, 0, 1, 1)
        self.all_tabs.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.all_tabs.tabBar().hide()
        self.all_tabs.setCurrentIndex(0)

        self.sidebar_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(30, 30, 30);}'
        )

        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_frame)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.exitor_layout = QtWidgets.QHBoxLayout()
        self.exitor_layout.setSpacing(10)

        self.exit_button = create_button(
            '',
            self.sidebar_frame,
            styles.EXIT_BUTTON,
            min_size=12,
            max_size=12,
            add_layout=self.exitor_layout,
        )

        self.collapse_button = create_button(
            '',
            self.sidebar_frame,
            styles.EXIT_BUTTON,
            min_size=12,
            max_size=12,
            add_layout=self.exitor_layout,
        )
        self.expand_button = create_button(
            '',
            self.sidebar_frame,
            styles.EXIT_BUTTON,
            min_size=12,
            max_size=12,
            add_layout=self.exitor_layout,
        )

        self.verticalLayout.addLayout(self.exitor_layout)
        self.sidebar_layout.setContentsMargins(20, 30, 20, 30)
        self.sidebar_layout.setSpacing(20)
        self.logo_button = create_button(
            '',
            self.sidebar_frame,
            min_size=50,
            max_size=50,
            add_layout=self.sidebar_layout,
        )
        self.logo_button.setStyleSheet(styles.sidebar_button('UI/icons/logo-icon.png'))
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.main_button = create_button(
            '',
            self.sidebar_frame,
            min_size=50,
            max_size=50,
            add_layout=self.sidebar_layout,
        )
        self.main_button.setStyleSheet(styles.sidebar_button('UI/icons/main-icon.png'))

        self.plus_button = create_button(
            '',
            self.sidebar_frame,
            min_size=50,
            max_size=50,
            add_layout=self.sidebar_layout,
        )
        self.plus_button.setStyleSheet(styles.sidebar_button('UI/icons/plus-icon.png'))

        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))

        self.settings_button = create_button(
            '',
            self.sidebar_frame,
            min_size=(50, 50),
            max_size=(50, 50),
            add_layout=self.sidebar_layout,
        )
        self.settings_button.setStyleSheet(
            styles.sidebar_button('UI/icons/settings-icon.png')
        )

        self.info_button = create_button(
            '',
            self.sidebar_frame,
            min_size=(50, 50),
            max_size=(50, 50),
            add_layout=self.sidebar_layout,
        )
        self.info_button.setStyleSheet(styles.sidebar_button('UI/icons/info-icon.png'))

        self.verticalLayout.addLayout(self.sidebar_layout)
        self.main_layout.addWidget(self.sidebar_frame, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.main_layout)
        self.setCentralWidget(self.main_window)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.all_tabs.setCurrentIndex(0)

        self.header_layout = QtWidgets.QGridLayout()
        self.setup_plus_header()
        self.setup_main_header()

    def setup_main_header(self):
        self.header_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(35, 35, 35);}'
        )
        self.header_horizontal_layout = create_layout(
            QHBoxLayout, [20, 5, 10, 5], 15, out_layout=self.header_frame
        )
        self.edit_button = create_button(
            '',
            self.header_frame,
            min_size=30,
            max_size=30,
            add_layout=self.header_horizontal_layout,
        )
        self.edit_button.setStyleSheet(styles.header_button('UI/icons/edit-icon.png'))
        if profile_manager.current_profile.id == 'profile_00':
            self.edit_button.hide()

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        self.notification = create_button(
            '',
            self.header_frame,
            min_size=[400, 30],
            max_size=30,
            add_layout=self.header_horizontal_layout,
        )
        self.notification.setStyleSheet(
            "QPushButton {color: rgb(186, 189, 182); background-color: rgb(120, 45, 20); border: 1px solid "
            "rgb(10, 40, 10); border-radius: 5; padding: 5px;}"
        )

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.header_layout = QtWidgets.QGridLayout()

        self.profile_button = create_button(
            'No Profile',
            self.header_frame,
            min_size=(0, 30),
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )
        self.profile_button.setStyleSheet(
            'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border: none;'
            'border-radius: 5px; padding: 0px 10px, 5px,} QPushButton:hover {background-color: rgb(45, 45, 45);}'
        )
        self.profile_button.setIcon(QIcon('UI/icons/expand-profile-icon.png'))
        self.profile_button.setIconSize(QSize(24, 24))
        self.profile_button.setLayoutDirection(Qt.RightToLeft)

        self.connect_button = create_button(
            '',
            self.header_frame,
            min_size=30,
            max_size=30,
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
        )
        self.connect_button.setStyleSheet(
            styles.header_button('UI/icons/connect-icon.png')
        )

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)
        self.edit_button.clicked.connect(self.open_edit_tab)

    def setup_plus_header(self):
        self.header_layout = QtWidgets.QGridLayout()

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 0, 1, 1)
        self.header_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(35, 35, 35);}'
        )

        self.header_horizontal_layout = QtWidgets.QHBoxLayout(self.header_frame)
        self.header_horizontal_layout.setContentsMargins(10, 5, 25, 5)
        self.header_horizontal_layout.setSpacing(20)

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        # self.notification = create_button(
        #     'You are wrong nigga!',
        #     self.header_frame,
        #     min_size=[400, 30],
        #     max_size=30,
        #     add_layout=self.header_horizontal_layout,
        #     add_params=[0, 1, 1, 1],
        # )
        # self.notification.setStyleSheet(
        #     "QPushButton {color: rgb(186, 189, 182); background-color: rgb(120, 45, 20); border: 1px solid "
        #     "rgb(10, 40, 10); border-radius: 5; padding: 5px;}"
        # )

        self.profile_name = create_label(
            'New Profile',
            self.header_frame,
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 2, 1, 1)

        self.save_plus_button = create_button(
            'Save',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
        )
        self.connect_plus_button = create_button(
            'Connect',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 4, 1, 1],
        )

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)
        self.save_plus_button.clicked.connect(self.save_new_profile)
        self.connect_plus_button.clicked.connect(self.save_profile_and_connect)

    def setup_edit_header(self):
        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 0, 1, 1)
        self.header_frame = QtWidgets.QFrame(self.main_window)
        self.header_frame.setStyleSheet(
            "QFrame {\n" "   background-color: rgb(35, 35, 35);\n" "}"
        )

        self.header_horizontal_layout = QtWidgets.QHBoxLayout(self.header_frame)
        self.header_horizontal_layout.setContentsMargins(10, 5, 25, 5)
        self.header_horizontal_layout.setSpacing(20)

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.header_layout = QtWidgets.QGridLayout()

        self.profile_name = create_label(
            'New Profile',
            self.header_frame,
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 2, 1, 1)

        self.save_edit_button = create_button(
            'Save',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
        )
        self.connect_button = create_button(
            'Connect',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 4, 1, 1],
        )

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)

        self.save_edit_button.clicked.connect(self.edit_tab.save_settings)
