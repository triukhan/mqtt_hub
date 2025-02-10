import sys

from PyQt5 import QtWidgets

from connections.main_window_connections import MainWindow
from mqtt.connector import MQTTConnector


class MqttHub(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = MQTTConnector()
        self.connect_button.clicked.connect(
            lambda: self.connector.start(self.current_profile.topics)
        )
        self.main_tab.publish_button.clicked.connect(
            lambda: self.connector.publish(
                self.current_profile.topics[0], self.main_tab.get_command_text()
            )
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MqttHub()
    window.show()
    sys.exit(app.exec_())
