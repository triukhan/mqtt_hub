from PyQt5.QtWidgets import QDialog

from GUI.dialogs.clipboard_dialog_ui import ClipboardDialogUI


class ClipboardDialog(QDialog, ClipboardDialogUI):
    def __init__(self, save_method, parent=None):
        super().__init__(parent)
        self.setup_ui(self)

        self.cancel()
        self._add()
        self.save_method = save_method

    def cancel(self):
        self.cancel_button.clicked.connect(self.close)

    def _add(self):
        self.save_button.clicked.connect(self.add_clipboard)

    def add_clipboard(self):
        name = self.name_field.text()
        self.save_method(name)
        self.close()
