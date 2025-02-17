from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem

from connections.clipboard_dialog_connections import ClipboardDialog
from GUI.tabs.main_tab_gui import MainTabUI
from settings.profile_manager import profile_manager


class MainTab(MainTabUI):
    def __init__(self):
        super().__init__()
        self.receiver_list.itemClicked.connect(self.display_message_from_receiver_list)
        self.add_clipboard_button.clicked.connect(self.show_clipboard_dialog)
        self.set_clipboard_messages()
        self.clipboard_list.currentItemChanged.connect(
            self.display_message_in_command_field
        )

    def get_command_text(self):
        return self.command_field.toPlainText()

    def display_message_from_receiver_list(self, item):
        payload = item.data(Qt.UserRole)
        self.receiver_text_edit.setPlainText(payload)

    def set_clipboard_messages(self):
        clipboard_messages = profile_manager.get_clipboard_messages()

        for message_name, message_text in clipboard_messages.items():
            item = QListWidgetItem()
            item.setText(message_name)
            item.setData(Qt.UserRole, message_text)
            self.clipboard_list.addItem(item)

    def display_message_in_command_field(self, item):
        command = item.data(Qt.UserRole)
        self.command_field.setPlainText(command)

    def save_message_to_clipboard(self, message_name: str):
        message_text = self.command_field.toPlainText()
        profile_manager.add_clipboard_message(message_name, message_text)
        item = QListWidgetItem()
        item.setText(message_name)
        item.setData(Qt.UserRole, message_text)
        self.clipboard_list.addItem(item)

    def show_clipboard_dialog(self):
        ClipboardDialog(self.save_message_to_clipboard, self).exec_()
