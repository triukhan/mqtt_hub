from PyQt5.QtCore import QEvent, QPropertyAnimation, QRect, QTimer
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QPushButton

from settings.profile_manager import profile_manager
from UI.main_window_ui import MqttHubUi


class MainWindow(MqttHubUi):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self.open_main_tab()

        self.connect_sidebar()
        self.setup_topics()
        self.update_profile_button()
        self._setup_notifications()
        self.disconnect = None

    @property
    def current_profile(self):
        return profile_manager.current_profile

    def save_new_profile(self):
        self._setup_notifications()
        # self.show_fail_notification('', 5) #todo: to validate settings
        settings = self.plus_tab.get_settings()
        profile_manager.create_profile(**settings)
        # self.disconnect() #TODO uncomment after disconnect
        self.clear_tab()
        self.show_positive_notification('Profile was successfully created')

    def clear_tab(self):
        self.open_main_tab()
        self.main_tab.set_clipboard_messages(new=True)
        self.main_tab.receiver_list.clear()
        self.main_tab.tags_widget.clear_tags()

    def open_main_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(0)
        self.setup_main_header()
        self.update_profile_button()
        self.select_button(self.main_button)

    def open_plus_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(1)
        self._setup_plus_header()
        self.select_button(self.plus_button)

    def open_edit_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(2)
        self._setup_edit_header()
        self.save_edit_button.clicked.connect(self.save_edit_profile)
        self.edit_tab.load_current_profile_settings()

    def save_edit_profile(self):
        self.clear_sidebar_selections()
        self.edit_tab.save_settings()
        self.open_main_tab()
        self.show_positive_notification('Settings were successfully saved')

    def open_settings_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(3)
        self.select_button(self.settings_button)

    def open_info_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(4)
        self.select_button(self.info_button)

    def connect_sidebar(self):
        self.main_button.clicked.connect(self.open_main_tab)
        self.plus_button.clicked.connect(self.open_plus_tab)
        self.settings_button.clicked.connect(self.open_settings_tab)
        self.info_button.clicked.connect(self.open_info_tab)
        self.exit_button.clicked.connect(self.close)

    def show_fail_notification(self, text=None, pos=10):
        self.notification.setStyleSheet(
            "QPushButton {color: rgb(186, 189, 182); background-color: rgb(120, 45, 20); border: 1px solid "
            "rgb(10, 40, 10); border-radius: 5; padding: 5px;}"
        )
        self.notification.setText(text or 'Fail')
        self._start_notification_animation(pos)

    def show_positive_notification(self, text='Success', pos=10):
        self.notification.setStyleSheet(
            "QPushButton {color: rgb(255, 250, 250); background-color: rgb(103, 159, 95); border: 1px solid "
            "rgb(10, 40, 10); border-radius: 5; padding: 5px;}"
        )
        if isinstance(text, str):
            self.notification.setText(text)
        else:
            self.notification.setText('Success')
        self._start_notification_animation(pos)

    def _setup_notifications(self):
        self.notification.setMouseTracking(True)
        self.notification.installEventFilter(self)
        self.notification_opacity = QGraphicsOpacityEffect(self.notification)
        self.notification.setGraphicsEffect(self.notification_opacity)
        self.notification.hide()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.fade_notification)
        self.main_tab.show_fail_message = self.show_fail_notification

    def setup_main_header(self):
        super()._setup_main_header()
        if profile_manager.current_profile.id == 'profile_00':
            self.edit_button.hide()
        self._setup_notifications()
        self.edit_button.clicked.connect(self.open_edit_tab)

    def fade_notification(self):
        self.opacity_fade = QPropertyAnimation(self.notification_opacity, b"opacity")
        self.opacity_fade.setDuration(250)
        self.opacity_fade.setStartValue(0.70)
        self.opacity_fade.setEndValue(0)
        self.opacity_fade.start()
        QTimer.singleShot(250, self.notification.hide)

    def _start_notification_animation(self, pos: int = 10):
        self.notification.show()
        self.notification_opacity.setOpacity(1)
        self.rolling_animation = QPropertyAnimation(self.notification, b"geometry")
        self.rolling_animation.setDuration(100)
        self.rolling_animation.setStartValue(QRect(230, 0, 0, 0))
        self.rolling_animation.setEndValue(QRect(230, pos, 100, 50))
        self.rolling_animation.start()
        self.timer.start(5000)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter and source == self.notification:
            self.timer.stop()
            self.notification_opacity.setOpacity(0.9)
        elif event.type() == QEvent.Leave and source == self.notification:
            self.timer.start(5000)
            self.notification_opacity.setOpacity(0.7)
        return super().eventFilter(source, event)

    @staticmethod
    def select_button(button: QPushButton):
        button.setStyleSheet(
            button.styleSheet() + 'QPushButton {background-color: rgb(40, 40, 40);}'
        )

    def clear_sidebar_selections(self):
        for button in (
            self.main_button,
            self.plus_button,
            self.settings_button,
            self.info_button,
        ):
            button.setStyleSheet(
                button.styleSheet() + 'QPushButton {background-color: rgb(30, 30, 30)}'
            )
