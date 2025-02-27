from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog, QDialog

from settings.topic import Topic
from UI.dialogs.topic_dialog_ui import TopicDialogUI


class TopicDialog(QDialog, TopicDialogUI):
    def __init__(self, save_method, parent, topic: Topic = None, tag: dict = None):
        super().__init__(parent)
        self._save_method = save_method
        self._tag = tag
        self._topic = topic

        self._setup_ui(self)
        self._set_color_button(Qt.gray)
        self._set_topic_settings()
        self._setup_connections()

    def _setup_connections(self):
        self.exit_button.clicked.connect(self.close)
        self.color_button.clicked.connect(self._open_color_picker)
        self.save_button.clicked.connect(self.save_and_close)
        self.cancel_button.clicked.connect(self.close)

    def _set_color_button(self, color):
        color_hex = color.name() if isinstance(color, QColor) else QColor(color).name()
        self.color_button.setStyleSheet(
            self.color_button.styleSheet() + f"QPushButton {{ color: {color_hex}; }}"
        )

    def _open_color_picker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self._set_color_button(color)
            self.color_field.setText(color.name())

    def _get_topic_settings(self):
        return {
            '_address': self.topic_field.text(),
            '_alias': self.alias_field.text(),
            '_qos': self.qos_field.text(),
            '_color': self.color_field.text(),
            '_no_local': self.no_local_checkbox.isChecked(),
            '_retain_as_published': self.retain_published_checkbox.isChecked(),
            '_retain_handling': self.retain_handling_field.text(),
        }, self._tag

    def _set_topic_settings(self):
        if not self._topic:
            return None

        self.topic_field.setText(self._topic.address)
        self.alias_field.setText(self._topic.alias)
        self.qos_field.setText(self._topic.qos or '1')
        self.color_field.setText(self._topic.color)
        self.no_local_checkbox.setChecked(self._topic.no_local == 'True')
        self.retain_published_checkbox.setChecked(
            self._topic.retain_as_published == 'True'
        )
        self.retain_handling_field.setText(self._topic.retain_handling)
        self._set_color_button(self._topic.color or Qt.gray)

    def save_and_close(self):
        self._save_method(self._topic, *self._get_topic_settings())
        self.close()
