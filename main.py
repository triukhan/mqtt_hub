import sys

from PyQt5 import QtWidgets

from GUI.main_window import MqttHubUi


class MqttHub(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MqttHubUi()
        self.ui.setup_ui(self)
        self.ui.settings_button.clicked.connect(
            lambda: self.ui.all_tabs.setCurrentIndex(2)
        )
        self.ui.info_button.clicked.connect(lambda: self.ui.all_tabs.setCurrentIndex(1))
        self.ui.main_button.clicked.connect(lambda: self.ui.all_tabs.setCurrentIndex(0))
        self.ui.plus_button.clicked.connect(lambda: self.ui.all_tabs.setCurrentIndex(3))
        self.ui.all_tabs.tabBar().hide()
        self.ui.all_tabs.setStyleSheet("QTabWidget::pane { border: 0; }")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MqttHub()
    window.show()
    sys.exit(app.exec_())
