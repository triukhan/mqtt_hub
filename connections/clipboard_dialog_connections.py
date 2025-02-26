from PyQt5.QtWidgets import QDialog

from UI.dialogs.clipboard_dialog_ui import ClipboardDialogUI


class ClipboardDialog(QDialog, ClipboardDialogUI):
    def __init__(self, save_method, parent=None):
        super().__init__(parent)
        self.save_method = save_method
        self._setup_ui(self)
        self._setup_connections()

    def _setup_connections(self):
        self.save_button.clicked.connect(self.add_clipboard)
        self.cancel_button.clicked.connect(self.close)

    def add_clipboard(self):
        name = self.name_field.text()
        text = self.text_field.toPlainText()
        self.save_method(name, text)
        self.close()
