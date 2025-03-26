from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import (
    QAction,
    QGridLayout,
    QHBoxLayout,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from qframelesswindow import FramelessWindow

from connections.main_tab_connections import MainTab
from connections.plus_tab_connections import EditTab, PlusTab
from settings.profile_manager import profile_manager
from UI.icons.icons import (
    CONNECT_ICON,
    DASH_ICON,
    EDIT_ICON,
    EXIT_ICON,
    EXPAND_HEAD_ICON,
    INFO_ICON,
    LOGO_ICON,
    MAIN_ICON,
    PAUSE_ICON,
    PLUS_ICON,
    SETTINGS_ICON,
)
from UI.interface_utils import (
    Spacer,
    create_button,
    create_expand_button,
    create_frame,
    create_label,
    create_layout,
    create_spacer,
    set_button_text,
)
from UI.styles import (
    EXIT_BUTTON,
    FRAME_COLOR,
    HEADER_FRAME,
    MAIN_BUTTON_WITHOUT_HOVER,
    MAIN_WINDOW,
    exit_button,
    header_button,
    sidebar_button,
)
from UI.tabs.info_tab_ui import InfoTab
from UI.tabs.settings_tab_ui import SettingsTabUi


class MqttHubUi(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 1066, 904)
        self.drag_pos = None
        self.main_tab = MainTab()
        self.plus_tab = PlusTab()
        self.edit_tab = EditTab()

    def _setup_ui(self):
        self.main_window = QWidget(self)
        self.main_window.setStyleSheet('QWidget {background-color: rgb(30, 30, 30);}')
        self.setStyleSheet(MAIN_WINDOW)

        self.horizontalLayout_2 = create_layout(
            QHBoxLayout, 0, out_layout=self.main_window
        )
        self.main_layout = create_layout(QGridLayout, spacing=0)
        self.main_w = create_layout(QGridLayout, spacing=0)

        self.tab_layout = create_layout(QGridLayout, spacing=0)
        self.all_tabs = QTabWidget(self.main_window)
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
        self.exit_layout = create_layout(QHBoxLayout, spacing=0)
        spacer = create_spacer(Spacer.HORIZONTAL)
        spacer.changeSize(7, 0)
        self.exit_layout.addItem(spacer)
        self.exit_button = create_button(
            '',
            self.sidebar_frame,
            12,
            12,
            self.exit_layout,
            style=EXIT_BUTTON,
            anim=False,
        )
        self.exit_button.installEventFilter(self)
        self.collapse_button = create_button(
            '',
            self.sidebar_frame,
            12,
            12,
            self.exit_layout,
            style=EXIT_BUTTON,
            anim=False,
        )
        self.collapse_button.installEventFilter(self)
        self.expand_button = create_button(
            '',
            self.sidebar_frame,
            12,
            12,
            self.exit_layout,
            style=EXIT_BUTTON,
            anim=False,
        )
        spacer = create_spacer(Spacer.HORIZONTAL)
        spacer.changeSize(7, 0)
        self.exit_layout.addItem(spacer)
        self.expand_button.installEventFilter(self)
        self.sidebar_vertical_layout.addLayout(self.exit_layout)

        self.sidebar_layout = create_layout(QVBoxLayout, [20, 30, 20, 30], 10)
        self.logo_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
            anim=False,
        )
        self.logo_button.setStyleSheet(sidebar_button(LOGO_ICON))
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.main_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
            body=True,
            style=sidebar_button(MAIN_ICON),
        )
        self.plus_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
            style=sidebar_button(PLUS_ICON),
            body=True,
        )
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.sidebar_layout.addItem(create_spacer(Spacer.VERTICAL))
        self.settings_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
            body=True,
            style=sidebar_button(SETTINGS_ICON),
        )
        self.info_button = create_button(
            '',
            self.sidebar_frame,
            50,
            50,
            self.sidebar_layout,
            body=True,
            style=sidebar_button(INFO_ICON),
        )
        self.sidebar_vertical_layout.addLayout(self.sidebar_layout)
        self.main_layout.addWidget(self.sidebar_frame, 0, 0, 1, 1)
        self.buttons = [self.exit_button, self.collapse_button, self.expand_button]

        self.horizontalLayout_2.addLayout(self.main_layout)
        self.setCentralWidget(self.main_window)

    def eventFilter(self, obj, event):
        if obj in self.buttons:
            if event.type() == QEvent.Enter:
                self.set_hover(True)
            elif event.type() == QEvent.Leave:
                if not any(btn.underMouse() for btn in self.buttons):
                    self.set_hover(False)
        return super().eventFilter(obj, event)

    def set_hover(self, hover):
        if not hover:
            for button in self.buttons:
                button.setStyleSheet(EXIT_BUTTON)
        else:
            self.exit_button.setStyleSheet(exit_button(EXIT_ICON))
            self.collapse_button.setStyleSheet(exit_button(DASH_ICON))
            self.expand_button.setStyleSheet(exit_button(EXPAND_HEAD_ICON))

    def _setup_main_header(self):
        self.header_frame = create_frame(
            self.main_window, 'QFrame {background-color: rgb(35, 35, 35);}'
        )
        self.header_horizontal_layout = create_layout(
            QHBoxLayout, [20, 5, 10, 5], 0, out_layout=self.header_frame
        )
        self.edit_button = create_button(
            '',
            self.header_frame,
            30,
            30,
            self.header_horizontal_layout,
            style=header_button(EDIT_ICON),
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.notification = create_button(
            '',
            self.header_frame,
            [400, 30],
            [400, 30],
            self.header_horizontal_layout,
            anim=False,
        )
        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        self.header_layout = create_layout(QGridLayout, spacing=6)
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
            style=header_button(CONNECT_ICON),
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)

    def _setup_plus_header(self):
        self.header_layout = QGridLayout()

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 0, 1, 1)
        self.header_frame = create_frame(self.main_window, FRAME_COLOR + HEADER_FRAME)

        self.header_horizontal_layout = QHBoxLayout(self.header_frame)
        self.header_horizontal_layout.setContentsMargins(0, 0, 10, 0)
        self.header_horizontal_layout.setSpacing(15)

        self.profile_name = create_label(
            '    New Profile',
            self.header_frame,
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )
        self.notification = create_button(
            '',
            self.header_frame,
            [400, 30],
            30,
            self.header_layout,
            [0, 1, 1, 1],
            anim=False,
        )
        self.notification.hide()

        self.header_layout.addItem(create_spacer(Spacer.HORIZONTAL), 0, 2, 1, 1)

        self.create_button = create_button(
            'Create',
            self.header_frame,
            min_size=[0, 30],
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
            style=MAIN_BUTTON_WITHOUT_HOVER,
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )
        self.connect_plus_button = create_button(
            'Connect',
            self.header_frame,
            min_size=[0, 30],
            add_layout=self.header_layout,
            add_params=[0, 4, 1, 1],
            style=MAIN_BUTTON_WITHOUT_HOVER,
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )

        self.header_horizontal_layout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)
        self.connect_plus_button.clicked.connect(self.save_profile_and_connect)

    def _setup_edit_header(self):
        self.header_frame = create_frame(self.main_window, FRAME_COLOR + HEADER_FRAME)

        self.header_horizontal_layout = QHBoxLayout(self.header_frame)
        self.header_horizontal_layout.setContentsMargins(0, 0, 10, 0)

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.notification = create_button(
            '',
            self.header_frame,
            [400, 30],
            30,
            self.header_horizontal_layout,
            anim=False,
        )
        self.notification.hide()

        self.profile_name = create_label(
            '  ' + profile_manager.current_profile.name, self.header_frame
        )
        self.profile_name.setAlignment(Qt.AlignCenter)
        self.header_horizontal_layout.addWidget(self.profile_name, 1)

        self.header_horizontal_layout.addItem(create_spacer(Spacer.HORIZONTAL))

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)

        self.save_edit_button = create_button(
            'Save',
            self.header_frame,
            style=MAIN_BUTTON_WITHOUT_HOVER + 'QPushButton {margin-right: 5px}',
            min_size=[0, 30],
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )
        self.connect_edit_button = create_button(
            'Connect',
            self.header_frame,
            style=MAIN_BUTTON_WITHOUT_HOVER,
            min_size=[0, 30],
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )

        self.buttons_layout.addWidget(self.save_edit_button)
        self.buttons_layout.addWidget(self.connect_edit_button)

        self.header_horizontal_layout.addLayout(self.buttons_layout)

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
        button, menu, show_menu = create_expand_button(
            text,
            layout,
            min_size=[0, 30],
            max_size=[200, 30],
            add_layout=add_layout,
            add_params=add_params,
            style=MAIN_BUTTON_WITHOUT_HOVER,
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )

        profiles = profile_manager.profiles
        for _, profile in profiles.items():
            if profile.is_default != 'None':
                continue
            font_metrics = QFontMetrics(button.font())
            elided_text = font_metrics.elidedText(profile.name, Qt.ElideRight, 110)

            action = QAction(elided_text, button)
            action.triggered.connect(lambda _, p=profile: self.set_profile(p))
            menu.addAction(action)

        button.clicked.connect(show_menu)

        return button

    def update_profile_button(self):
        text = profile_manager.current_profile.name
        set_button_text(self.profile_button, text, 100)

    def set_profile(self, profile):
        if profile == profile_manager.current_profile:
            return None
        self.edit_button.show()
        profile_manager.switch_profile(profile.id)
        self.main_tab.set_clipboard_messages()
        self.update_profile_button()
        self.clear_topics()
        self._setup_topics()

    def _setup_topics(self):
        for topic in profile_manager.current_profile.topics:
            self.main_tab.tags_widget.add_tag(topic)

    def clear_topics(self):
        self.main_tab.tags_widget.clear_tags()

    def change_connect_button(self, connect):
        if connect:
            self.connect_button.setStyleSheet(header_button(PAUSE_ICON))
        else:
            self.connect_button.setStyleSheet(header_button(CONNECT_ICON))
