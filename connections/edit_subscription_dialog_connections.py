from PyQt5.QtWidgets import QDialog

from GUI.dialogs.edit_subscribtion_dialog_ui import EditSubscribeDialogUI


class EditSubscribeDialog(QDialog, EditSubscribeDialogUI):
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.setup_ui(self)

        self.settings = settings
