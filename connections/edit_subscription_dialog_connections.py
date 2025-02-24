from PyQt5.QtWidgets import QDialog

from GUI.dialogs.edit_subscribtion_dialog_ui import EditSubscribeDialogUI


class EditSubscribeDialog(QDialog, EditSubscribeDialogUI):
    def __init__(self, save_method, parent=None):
        super().__init__(parent)
        self.save_method = save_method
        self.setup_ui(self)
        self.save_topic_button.clicked.connect(self.save_and_close)

    def get_topic_settings(self):
        return {
            '_address': self.topic_field.text(),
            '_alias': self.alias_field.text(),
            '_qos': self.qos_field.text(),
            '_color': self.color_field.text(),
            '_no_local': self.no_local_checkbox.isChecked(),
            '_retain_as_published': self.retain_published_checkbox.isChecked(),
            '_retain_handling': self.retain_handling_field.text(),
        }

    def save_and_close(self):
        self.save_method(self.get_topic_settings())
        self.close()
