from contextlib import suppress

from PyQt5.QtCore import QEvent, QPropertyAnimation, QRect, QTimer
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QWidget

from connections.connection_utils import Result
from settings.profile_manager import profile_manager
from UI.dialogs.confirmation_dialog import ConfirmationDialogUI
from UI.main_window_ui import MqttHubUi
from UI.styles import COMMON_NOTIFY, FAIL_NOTIFY, SUCCESS_NOTIFY


class MainWindow(MqttHubUi):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self.open_main_tab()
        self.disconnect = None

        self.connect_sidebar()
        self._setup_topics()
        self.update_profile_button()
        self._setup_overlay()

        self.edit_tab.delete_button.clicked.connect(
            lambda: self.open_delete_dialog(self.delete_profile)
        )

    def _setup_overlay(self):
        self.overlay = QWidget(self)
        self.overlay.setGeometry(0, 0, self.width(), self.height())
        self.overlay.setStyleSheet('background-color: rgba(0, 0, 0, 100);')
        self.overlay.hide()

    def save_new_profile(self, with_notify: bool = True):
        self._setup_notifications()
        settings = self.plus_tab.get_settings()
        if (error_msg := self.validate_settings(settings)) is not None:
            self.show_notification(error_msg, Result.COMMON, 5)
            return

        profile_manager.create_profile(**settings)
        self.disconnect()
        self.clear_tab()
        if with_notify:
            self.show_notification('Profile was successfully created', Result.SUCCESS)

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
        self.main_button.select()

    def open_plus_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(1)
        self._setup_plus_header()
        self.plus_button.select()

    def open_edit_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(2)
        self._setup_edit_header()
        self.save_edit_button.clicked.connect(self.save_edit_profile)
        self.connect_edit_button.clicked.connect(
            self.save_settings_edit_tab_and_connect
        )
        self.edit_tab.load_current_profile_settings()

    def save_edit_profile(self, with_notify: bool = True):
        self.clear_sidebar_selections()
        self.edit_tab.save_settings()
        self.open_main_tab()
        if with_notify:
            self.show_notification('Settings were successfully saved', Result.SUCCESS)

    def open_settings_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(3)
        self.settings_button.select()

    def open_info_tab(self):
        self.clear_sidebar_selections()
        self.all_tabs.setCurrentIndex(4)
        self.info_button.select()

    def connect_sidebar(self):
        self.main_button.clicked.connect(self.open_main_tab)
        self.plus_button.clicked.connect(self.open_plus_tab)
        self.settings_button.clicked.connect(self.open_settings_tab)
        self.info_button.clicked.connect(self.open_info_tab)
        self.exit_button.clicked.connect(self.close)

    def show_notification(self, text: str, res: Result, pos: int = 10):
        match res:
            case Result.SUCCESS:
                self.notification.setStyleSheet(SUCCESS_NOTIFY)
            case Result.FAILURE:
                self.notification.setStyleSheet(FAIL_NOTIFY)
            case Result.COMMON:
                self.notification.setStyleSheet(COMMON_NOTIFY)

        if isinstance(text, str):
            self.notification.setText(text)
        else:
            raise TypeError('You need to pass str to the notification')

        self._start_notification_animation(pos, 3000)

    def _setup_notifications(self):
        self.notification.setMouseTracking(True)
        self.notification.installEventFilter(self)
        self.notification_opacity = QGraphicsOpacityEffect(self.notification)
        self.notification.setGraphicsEffect(self.notification_opacity)
        self.notification.hide()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.fade_notification)
        self.main_tab.notification_displayer = self.show_notification

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
        with suppress(AttributeError):
            QTimer.singleShot(250, self.profile_name.show)

    def _start_notification_animation(self, pos: int = 10, duration=5000):
        with suppress(AttributeError):
            self.profile_name.hide()
        self.notification.show()
        self.notification_opacity.setOpacity(0.70)
        self.rolling_animation = QPropertyAnimation(self.notification, b"geometry")
        self.rolling_animation.setDuration(100)
        self.rolling_animation.setStartValue(QRect(230, 0, 0, 0))
        self.rolling_animation.setEndValue(QRect(230, pos, 100, 50))
        self.rolling_animation.start()
        self.timer.start(duration)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter and source == self.notification:
            self.timer.stop()
            self.notification_opacity.setOpacity(0.9)
        elif event.type() == QEvent.Leave and source == self.notification:
            self.timer.start(5000)
            self.notification_opacity.setOpacity(0.7)
        return super().eventFilter(source, event)

    def clear_sidebar_selections(self):
        for button in (
            self.main_button,
            self.plus_button,
            self.settings_button,
            self.info_button,
        ):
            button.deselect()

    def validate_settings(self, settings: dict):
        if settings['self_signed'] and not all(
            [settings['ca_file'], settings['crt_file'], settings['key_file']]
        ):
            return 'SSL/TLS: You need to fill in certificates'
        if settings['port'] and not settings['port'].strip().isdigit():
            return 'Port should be a number'

    def open_delete_dialog(self, method):
        self.overlay.show()
        ConfirmationDialogUI(
            self, 'Are you sure you want to delete this message?', method
        ).exec_()
        self.overlay.hide()

    def handle_delete_message(self):
        if (item := self.main_tab.get_selected_item()) is not None:
            self.open_delete_dialog(
                lambda: self.main_tab.delete_clipboard_message(item)
            )
            self.show_notification('Message is deleted', Result.COMMON)
        else:
            self.show_notification('You are not selected any message', Result.COMMON)

    def set_profile(self, profile):
        super().set_profile(profile)
        self.disconnect()
