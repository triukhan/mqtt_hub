from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem

from connections.clipboard_dialog_connections import ClipboardDialog
from connections.topic_dialog_connections import TopicDialog
from UI.tabs.main_tab_ui import MainTabUI, TagsWidget
from settings.profile_manager import profile_manager
from settings.topic import Topic


class MainTab(MainTabUI):
    def __init__(self):
        super().__init__()

        self.tags_widget = TagsWidget(self.bottom_frame, self.show_edit_topic_dialog)
        self.add_button = self.tags_widget.add_button
        self.verticalLayout_3.addWidget(self.tags_widget)

        self.receiver_list.itemClicked.connect(self.display_message_from_receiver_list)
        self.add_clipboard_button.clicked.connect(self.show_clipboard_dialog)
        self.set_clipboard_messages()
        self.clipboard_list.currentItemChanged.connect(
            self.display_message_in_command_field
        )
        self.add_button.clicked.connect(self.create_topic)

    def create_topic(self):
        self.show_edit_subscription_dialog()

    def get_command_text(self):
        return self.command_field.toPlainText()

    def display_message_from_receiver_list(self, item):
        payload = item.data(Qt.UserRole)
        self.receiver_text_edit.setPlainText(payload)

    def set_clipboard_messages(self):
        clipboard_messages = profile_manager.current_profile.clipboard

        for message_name, message_text in clipboard_messages.items():
            item = QListWidgetItem()
            item.setText(message_name)
            item.setData(Qt.UserRole, message_text)
            self.clipboard_list.addItem(item)

    def display_message_in_command_field(self, item):
        command = item.data(Qt.UserRole)
        self.command_field.setPlainText(command)

    def save_message_to_clipboard(self, message_name: str, message_text: str):
        profile_manager.current_profile.add_clipboard(message_name, message_text)
        item = QListWidgetItem()
        item.setText(message_name)
        item.setData(Qt.UserRole, message_text)
        self.clipboard_list.addItem(item)

    def show_clipboard_dialog(self):
        ClipboardDialog(self.save_message_to_clipboard, self).exec_()

    def save_and_subscribe_topic(self, _, topic_settings: dict, __):
        topic = profile_manager.current_profile.add_topic(topic_settings)
        self.tags_widget.add_tag(topic)

    def setup_topics(self):
        for topic in profile_manager.current_profile.topics:
            self.tags_widget.add_tag(topic)

    def save_topic(self, topic: Topic, new_settings: dict, tag_dict: dict):
        topic.set_fields_from_dict(new_settings)
        tag_dict['label'].setText(topic.get_name())
        if color := topic.color:
            tag_dict['frame'].setStyleSheet(
                tag_dict['frame'].styleSheet()
                + f'QFrame {{border-left: 2px solid {color};}} QFrame:hover {{border-left: 2px solid {color};}}'
            )

    def show_edit_subscription_dialog(self):
        TopicDialog(self.save_and_subscribe_topic, self).exec_()

    def show_edit_topic_dialog(self, topic, tag_dict):
        TopicDialog(self.save_topic, self, topic, tag_dict).exec_()
