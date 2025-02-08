import sys

from PyQt5 import QtWidgets

from connections.main_window import MainWindow
from mqtt.connector import MQTTConnector

topics = [
    'cmd/smartis/ajax/hub/00186A94',
    'cmd/smartis/ajax/hub/00186A94/res',
    'dt/smartis/ajax/hub/00186A94',
]


class MqttHub(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = MQTTConnector()
        self.connect_button.clicked.connect(self.connector.start)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MqttHub()
    window.show()
    sys.exit(app.exec_())
