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

        self.connect_button.clicked.connect(
            lambda: self.connector.start(self.current_profile.topics)
        )
        self.main_tab.publish_button.clicked.connect(
            lambda: self.connector.publish(
                self.current_profile.topics[0], self.main_tab.get_command_text()
            )
        )

    def update_list_widget(self, topic, payload):
        item = QtWidgets.QListWidgetItem(topic)
        item.setData(Qt.UserRole, payload)
        self.main_tab.receiver_list.addItem(item)
        item.setSelected(True)
        self.main_tab.receiver_text_edit.setPlainText(payload)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MqttHub()
    window.show()
    sys.exit(app.exec_())
