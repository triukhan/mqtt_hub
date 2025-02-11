from PyQt5.QtCore import Qt

from GUI.tabs.main_tab_gui import MainTabUI


class MainTab(MainTabUI):
    def __init__(self):
        super().__init__()
        self.receiver_list.itemClicked.connect(self.display_message_from_receiver_list)

    def get_command_text(self):
        return self.command_field.toPlainText()

    def display_message_from_receiver_list(self, item):
        payload = item.data(Qt.UserRole)
        self.receiver_text_edit.setPlainText(payload)
