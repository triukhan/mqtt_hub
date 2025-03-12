import sys
from contextlib import suppress

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QApplication

from connections.main_window_connections import MainWindow
from mqtt.connector import MQTTMixin
from settings.profile_manager import profile_manager
from UI.interface_utils import BorderDelegate


class MqttHub(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = MQTTMixin()

        self.connector.message_received.connect(self.update_list_widget)
        self.connector.notification_signal.connect(self.show_positive_notification)
        self.connector.connected_signal.connect(self.change_connect_button)
        self.connector.common_signal.connect(self.show_common_notification)
        self.disconnect = self.connector.stop

        self.main_tab.publish_button.clicked.connect(
            lambda: self.connector.publish(
                profile_manager.topic_to_publish, self.main_tab.get_command_text()
            )
        )
        self.main_tab.unsubscribe_topic = self.connector.unsubscribe
        self.main_tab.connector = self.connector

        self.edit_tab.delete_button.clicked.connect(self.delete_profile)
        self.main_tab.receiver_list.setItemDelegate(
            BorderDelegate(self.main_tab.receiver_list)
        )

    def setup_main_header(self):
        super().setup_main_header()
        with suppress(AttributeError):
            self.change_connect_button(self.connector.is_connected)
        self.connect_button.clicked.connect(self.handle_connect_click)

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
        item = QListWidgetItem(topic)
        color = profile_manager.current_profile.find_topic_by_address(topic).color
        item.setData(Qt.UserRole, [payload, color])
        self.main_tab.receiver_list.addItem(item)
        self.main_tab.receiver_list.scrollToItem(self.main_tab.receiver_list.item(self.main_tab.receiver_list.count() - 1)) # todo: here is autoscroll
        item.setSelected(True)
        self.main_tab.receiver_text_edit.setPlainText(payload)

    def save_profile_and_connect(self):
        self.save_new_profile()
        self.main_tab.tags_widget.clear_tags()
        self.connector.start(profile_manager.current_profile)

    def delete_profile(self):
        profile_manager.delete_current_profile()
        # self.disconnect() #TODO uncomment after disconnect
        self.clear_tab()
        self.show_positive_notification('Profile was successfully deleted')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MqttHub()
    window.show()
    sys.exit(app.exec_())
