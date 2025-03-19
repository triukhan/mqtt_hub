import sys
from contextlib import suppress

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMainWindow

from connections.main_window_connections import MainWindow
from mqtt.connector import MQTTMixin
from settings.profile_manager import profile_manager
from UI.interface_utils import BorderDelegate, JsonHighlighter


class MqttHub(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = MQTTMixin()
        self.connector.message_received.connect(self.update_list_widget)
        self.connector.connected_signal.connect(self.change_connect_button)
        self.connector.success_signal.connect(self.show_positive_notification)
        self.connector.fail_signal.connect(self.show_fail_notification)
        self.connector.common_signal.connect(self.show_common_notification)
        self.main_tab.success_signal.connect(self.show_positive_notification)

        self.disconnect = self.connector.stop

        self.main_tab.publish_button.clicked.connect(
            lambda: self.connector.publish(
                profile_manager.topic_to_publish, self.main_tab.get_command_text()
            )
        )
        self.main_tab.unsubscribe_topic = self.connector.unsubscribe
        self.main_tab.connector = self.connector
        self.main_tab.receiver_list.setItemDelegate(
            BorderDelegate(self.main_tab.receiver_list)
        )
        self.select_message = False
        self.main_tab.select_toggle.stateChanged.connect(self.set_select_flag)

    def set_select_flag(self, state):
        self.select_message = state

    def setup_main_header(self):
        super().setup_main_header()
        with suppress(AttributeError):
            self.change_connect_button(self.connector.is_connected)
        self.connect_button.clicked.connect(self.handle_connect_click)

    def setup_edit_header(self):
        super()._setup_edit_header()
        self.connect_button.clicked.connect(self.save_profile_and_connect)

    def handle_connect_click(self):
        if self.connector.is_connected:
            self.connector.stop()
        else:
            self.start_connection()

    def start_connection(self):
        if profile_manager.current_profile.is_default == 'True':
            self.show_fail_notification('You need to create a profile first')
            return

        try:
            self.connector.start(profile_manager.current_profile)
        except Exception as e:
            self.show_fail_notification(f'Error: {e}')

    def update_list_widget(self, topic, payload):
        topic = profile_manager.current_profile.find_topic_by_address(topic)
        item = QListWidgetItem(topic.alias or topic.address)
        item.setData(Qt.UserRole, [payload, topic.color])
        self.main_tab.receiver_list.addItem(item)
        if profile_manager.current_profile.autoscroll:
            self.main_tab.receiver_list.scrollToItem(
                self.main_tab.receiver_list.item(
                    self.main_tab.receiver_list.count() - 1
                )
            )
        if not self.select_message:
            item.setSelected(True)
            self.main_tab.receiver_text_edit.setPlainText(payload)

        self.highlighter = JsonHighlighter(self.main_tab.receiver_text_edit.document())

    def save_profile_and_connect(self):
        self.save_new_profile(with_notify=False)
        self.main_tab.tags_widget.clear_tags()
        self.start_connection()

    def save_settings_edit_tab_and_connect(self):
        self.save_edit_profile(with_notify=False)
        self.start_connection()

    def delete_profile(self):
        profile_manager.delete_current_profile()
        self.disconnect()
        self.clear_tab()
        self.show_positive_notification('Profile was successfully deleted')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MqttHub()
    window.show()
    sys.exit(app.exec_())
