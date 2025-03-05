from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtGui import QFontMetrics, QIcon
from PyQt5.QtWidgets import (
    QAction,
    QGridLayout,
    QHBoxLayout,
    QMenu,
    QVBoxLayout,
    QWidget,
)

from connections.main_tab_connections import MainTab
from connections.plus_tab_connections import EditTab, PlusTab
from settings.profile_manager import profile_manager
from UI import styles
from UI.icons.icons import (
    CONNECT_ICON,
    EDIT_ICON,
    EXPAND_ICON,
    INFO_ICON,
    LOGO_ICON,
    MAIN_ICON,
    PLUS_ICON,
    SETTINGS_ICON,
)
from UI.interface_utils import (
    Spacer,
    create_button,
    create_frame,
    create_label,
    create_layout,
    create_spacer,
    set_button_text,
)
from UI.styles import MENU, sidebar_button
from UI.tabs.info_tab_ui import InfoTab
from UI.tabs.settings_tab_ui import SettingsTabUi


class MqttHubUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 50, 1066, 904)
        self.drag_pos = None
        self.main_tab = MainTab()
        self.plus_tab = PlusTab()
        self.edit_tab = EditTab()

    def _setup_ui(self):
        self.main_window = QtWidgets.QWidget(self)
        self.main_window.setStyleSheet('QWidget {background-color: rgb(30, 30, 30);}')

        self.horizontalLayout_2 = create_layout(
            QHBoxLayout, 0, out_layout=self.main_window
        )
        self.main_layout = create_layout(QGridLayout, spacing=0)
        self.main_w = create_layout(QGridLayout, spacing=0)

        self.tab_layout = create_layout(QGridLayout, spacing=0)
        self.all_tabs = QtWidgets.QTabWidget(self.main_window)
        self.all_tabs.setStyleSheet('QTabWidget::pane {border: 0;}')
        self.all_tabs.tabBar().hide()
        for tab in [
            self.main_tab,
            self.plus_tab,
            self.edit_tab,
            SettingsTabUi(),
            InfoTab(),
        ]:
            self.all_tabs.addTab(tab, '')
        self.tab_layout.addWidget(self.all_tabs, 0, 0, 1, 1)
        self.main_w.addLayout(self.tab_layout, 1, 0, 1, 1)

        self.sidebar_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(30, 30, 30);}'
        )

        self.sidebar_vertical_layout = create_layout(
            QVBoxLayout, [0, 10, 0, 0], 0, self.sidebar_frame
        )
        self.exit_layout = create_layout(QHBoxLayout, spacing=10)
        self.exit_button = create_button(
            '',
            self.sidebar_frame,
            12,
            12,
            self.exit_layout,
            style=styles.EXIT_BUTTON,
        )
        self.collapse_button = create_button(
            '',
            self.sidebar_frame,
            12,
            12,
            self.exit_layout,
            style=styles.EXIT_BUTTON,
        )
        self.expand_button = create_button(
            '',
            self.sidebar_frame,
            12,
            12,
            self.exit_layout,
            style=styles.EXIT_BUTTON,
        )
        self.sidebar_vertical_layout.addLayout(self.exit_layout)

        self.sidebar_layout = create_layout(QVBoxLayout, [20, 30, 20, 30], 20)
        self.logo_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
        )
        self.logo_button.setStyleSheet(styles.sidebar_button(LOGO_ICON))
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.main_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
        )
        self.main_button.setStyleSheet(styles.sidebar_button(MAIN_ICON))
        self.plus_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
        )
        self.plus_button.setStyleSheet(sidebar_button(PLUS_ICON))
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.settings_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
        )
        self.settings_button.setStyleSheet(styles.sidebar_button(SETTINGS_ICON))
        self.info_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
        )
        self.info_button.setStyleSheet(styles.sidebar_button(INFO_ICON))
        self.sidebar_vertical_layout.addLayout(self.sidebar_layout)
        self.main_layout.addWidget(self.sidebar_frame, 0, 0, 1, 1)

        self.horizontalLayout_2.addLayout(self.main_layout)
        self.setCentralWidget(self.main_window)
        # self.setup_plus_header() #TODO testing it

    def _setup_main_header(self):
        self.header_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(35, 35, 35);}'
        )
        self.header_horizontal_layout = create_layout(
            QHBoxLayout, [20, 5, 10, 5], 100, out_layout=self.header_frame
        )
        self.edit_button = create_button(
            '',
            self.header_frame,
            30,
            30,
            self.header_horizontal_layout,
        )
        self.edit_button.setStyleSheet(styles.header_button(EDIT_ICON))

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.notification = create_button(
            '',
            self.header_frame,
            [400, 30],
            30,
            self.header_horizontal_layout,
        )
        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        self.header_layout = create_layout(QGridLayout, spacing=12)
        self.profile_button = self.create_profile_button(
            'No Profile',
            self.header_frame,
            self.header_layout,
            [0, 1, 1, 1],
        )
        self.connect_button = create_button(
            '',
            self.header_frame,
            30,
            30,
            self.header_layout,
            [0, 3, 1, 1],
        )
        self.connect_button.setStyleSheet(styles.header_button(CONNECT_ICON))

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)

    def _setup_plus_header(self):
        self.header_layout = QtWidgets.QGridLayout()

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 0, 1, 1)
        self.header_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(35, 35, 35);}'
        )

        self.header_horizontal_layout = QtWidgets.QHBoxLayout(self.header_frame)
        self.header_horizontal_layout.setContentsMargins(10, 5, 25, 5)
        self.header_horizontal_layout.setSpacing(20)

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        self.profile_name = create_label(
            'New Profile',
            self.header_frame,
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 2, 1, 1)

        self.create_button = create_button(
            'Create',
            self.header_frame,
            style=styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
        )
        self.connect_plus_button = create_button(
            'Connect',
            self.header_frame,
            style=styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 4, 1, 1],
        )

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)
        self.create_button.clicked.connect(self.save_new_profile)
        self.connect_plus_button.clicked.connect(self.save_profile_and_connect)

    def _setup_edit_header(self):
        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 0, 1, 1)
        self.header_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(35, 35, 35);}'
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
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
            style=styles.MAIN_BUTTON,
        )
        self.connect_button = create_button(
            'Connect',
            self.header_frame,
            add_layout=self.header_layout,
            add_params=[0, 4, 1, 1],
            style=styles.MAIN_BUTTON,
        )

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)

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

    def create_profile_button(self, text, layout, add_layout, add_params: list):
        button = create_button(
            text,
            layout,
            min_size=(0, 30),
            add_layout=add_layout,
            add_params=add_params,
        )

        button.setIcon(QIcon(EXPAND_ICON))
        button.setIconSize(QSize(24, 24))
        button.setLayoutDirection(Qt.RightToLeft)

        button.setStyleSheet(
            'QPushButton {'
            'color: rgb(186, 189, 182);'
            'background-color: rgb(35, 35, 35);'
            'border-radius: 5px;'
            'padding: 5px'
            '} '
            'QPushButton:hover {background-color: rgb(45, 45, 45);}'
            'QPushButton::menu-indicator { image: none; }'
        )

        menu = QMenu()

        profiles = profile_manager.profiles
        for _, profile in profiles.items():
            if profile.is_default == 'True':
                continue
            font_metrics = QFontMetrics(button.font())
            elided_text = font_metrics.elidedText(profile.name, Qt.ElideRight, 110)

            action = QAction(elided_text, button)
            action.triggered.connect(lambda _, p=profile: self.set_profile(p))
            menu.addAction(action)

        def show_menu():
            menu.setStyleSheet(MENU)
            menu.setMinimumWidth(button.width())
            menu.setMaximumWidth(150)
            menu.popup(button.mapToGlobal(QPoint(0, button.height())))

        button.clicked.connect(show_menu)

        return button

    def update_profile_button(self):
        text = profile_manager.current_profile.name or 'No Name'
        set_button_text(self.profile_button, text, 100)

    def set_profile(self, profile):
        if profile == profile_manager.current_profile:
            return None
        profile_manager.switch_profile(profile.id)
        self.main_tab.set_clipboard_messages()
        self.update_profile_button()
        self.clear_topics()
        self.setup_topics()

    def setup_topics(self):
        for topic in profile_manager.current_profile.topics:
            self.main_tab.tags_widget.add_tag(topic)

    def clear_topics(self):
        self.main_tab.tags_widget.clear_tags()
