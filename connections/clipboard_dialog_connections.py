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
    def __init__(self, save_method, data, parent=None):
        super().__init__(parent)
        self.save_method = save_method
        self._setup_ui(self, True)
        self._setup_connections()
        self._set_fields(data[0], data[1][0])
        self.message_id = data[1][1]
        self.start_data = self._get_start_data()

    def _setup_connections(self):
        self.save_button.clicked.connect(self.add_clipboard)
        self.cancel_button.clicked.connect(self.close)

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
