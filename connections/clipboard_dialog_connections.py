from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from UI.dialogs.clipboard_dialog_ui import ClipboardDialogUI


class ClipboardDialog(QDialog, ClipboardDialogUI):
    def __init__(self, save_method, parent=None, with_delete=True):
        super().__init__(parent)
        self.save_method = save_method
        self._setup_ui(self, with_delete)
        self._setup_connections()

    def _setup_connections(self):
        self.save_button.clicked.connect(self.add_clipboard)
        self.cancel_button.clicked.connect(self.close)
        self.exit_button.clicked.connect(self.close)

    def add_clipboard(self):
        name = self.name_field.text()
        text = self.text_field.toPlainText()
        self.save_method(name, text)
        self.close()


class ClipboardEditDialog(QDialog, ClipboardDialogUI):
    def __init__(self, save_method, item, parent=None, delete_method=None):
        super().__init__(parent)
        self.save_method = save_method
        self.delete_method = delete_method

        self.item = item
        self.item_data = item.data(Qt.UserRole)
        self.message_id, self.message_text, self.message_name = (
            self.item_data[1],
            self.item_data[0],
            item.data(Qt.DisplayRole),
        )
        self._setup_ui(self, True)
        self._setup_connections()
        self._set_fields(self.message_name, self.message_text)
        self.start_data = self._get_start_data()

    def delete_met(self):
        self.delete_method(self.message_id, self.item)
        self.close()

    def _setup_connections(self):
        self.save_button.clicked.connect(self.add_clipboard)
        self.cancel_button.clicked.connect(self.close)
        self.delete_button.clicked.connect(self.delete_met)

    def _get_start_data(self):
        return [self.name_field.text(), self.text_field.toPlainText()]

    def add_clipboard(self):
        name = self.name_field.text()
        text = self.text_field.toPlainText()
        self.save_method(self.start_data, self.message_id, name, text)
        self.close()

    def _set_fields(self, name: str, data: str):
        self.name_field.setText(name)
        self.text_field.setPlainText(data)
