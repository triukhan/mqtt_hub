import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from connections.main_window_connections import MainWindow
from mqtt.connector import MQTTMixin


class MqttHub(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = MQTTMixin()

        self.connector.message_received.connect(self.update_list_widget)
        self.connector.notification_signal.connect(self.show_positive_notification)

        self.main_tab.publish_button.clicked.connect(
            lambda: self.connector.publish(self.main_tab.get_command_text())
        )

    def setup_main_header(self):
        super().setup_main_header()
        self.connect_button.clicked.connect(self.start_connection)

    def start_connection(self):
        try:
            self.connector.start(self.current_profile.topics)
        except Exception as e:
            self.show_fail_notification(f'Error: {e}')

    def update_list_widget(self, topic, payload):
        item = QtWidgets.QListWidgetItem(topic)
        item.setData(Qt.UserRole, payload)
        self.main_tab.receiver_list.addItem(item)
        item.setSelected(True)
        self.main_tab.receiver_text_edit.setPlainText(payload)

    def save_profile_and_connect(self):
        self.save_new_profile()
        self.connector.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MqttHub()
    window.show()
    sys.exit(app.exec_())
