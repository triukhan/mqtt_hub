from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog, QDialog

from GUI.dialogs.edit_subscribtion_dialog_ui import EditTopicDialogUI
from settings.topic import Topic


class EditSubscribeDialog(QDialog, EditTopicDialogUI):
    def __init__(self, save_method, parent=None, topic: Topic = None, tag: dict = None):
        super().__init__(parent)
        self.tag = tag
        self.save_method = save_method
        self.topic = topic
        self.setup_ui(self)
        self.save_topic_button.clicked.connect(self.save_and_close)
        if self.topic:
            self.set_topic_settings()
            self.set_color_button(topic.color or Qt.gray)
        else:
            self.set_color_button(Qt.gray)

        self.color_button.clicked.connect(self.open_color_picker)

    def set_color_button(self, color):
        color_hex = color.name() if isinstance(color, QColor) else QColor(color).name()
        self.color_button.setStyleSheet(
            self.color_button.styleSheet() + f"QPushButton {{ color: {color_hex}; }}"
        )

    def open_color_picker(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.set_color_button(color)
            self.color_field.setText(color.name())

    def get_topic_settings(self):
        return {
            '_address': self.topic_field.text(),
            '_alias': self.alias_field.text(),
            '_qos': self.qos_field.text(),
            '_color': self.color_field.text(),
            '_no_local': self.no_local_checkbox.isChecked(),
            '_retain_as_published': self.retain_published_checkbox.isChecked(),
            '_retain_handling': self.retain_handling_field.text(),
        }, self.tag

    def set_topic_settings(self):
        self.topic_field.setText(self.topic.address)
        self.alias_field.setText(self.topic.alias)
        self.qos_field.setText(self.topic.qos or '1')
        self.color_field.setText(self.topic.color)
        self.no_local_checkbox.setChecked(self.topic.no_local == 'True')
        self.retain_published_checkbox.setChecked(
            self.topic.retain_as_published == 'True'
        )
        self.retain_handling_field.setText(self.topic.retain_handling)

    def save_and_close(self):
        self.save_method(self.topic, *self.get_topic_settings())
        self.close()
