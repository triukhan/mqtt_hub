from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QAction, QListWidgetItem

from connections.clipboard_dialog_connections import (
    ClipboardDialog,
    ClipboardEditDialog,
)
from connections.connection_utils import Result
from connections.topic_dialog_connections import TopicDialog
from settings.profile_manager import profile_manager
from settings.topic import Topic
from UI.custom_widgets.tags_widget import TagsWidget
from UI.tabs.main_tab_ui import MainTabUI


class MainTab(MainTabUI):
    notification_signal = pyqtSignal(str, Result)

    def __init__(self):
        super().__init__()
        self.unsubscribe_topic = None
        self.clipboard_list.set_method(self.show_clipboard_dialog_with_settings)
        self.autoscroll_toggle.setChecked(profile_manager.current_profile.autoscroll)
        self.tags_widget = TagsWidget(self.bottom_frame, self.show_edit_topic_dialog)
        self.add_button = self.tags_widget.add_button
        self.verticalLayout_3.addWidget(self.tags_widget)

        self.receiver_list.itemClicked.connect(self.display_message_from_receiver_list)
        self.receiver_list.currentItemChanged.connect(
            self.display_message_from_receiver_list
        )

        self.add_clipboard_button.clicked.connect(self.show_clipboard_dialog)
        self.set_clipboard_messages()
        self.clipboard_list.currentItemChanged.connect(
            self.display_message_in_command_field
        )
        self.add_button.clicked.connect(self.create_topic)
        self.clear_button.clicked.connect(self.clear_list_and_message)
        self.connector = None

        for convert_format in ('JSON', 'Plaintext', 'Hex', 'Base64'):
            font_metrics = QFontMetrics(self.convertor_button.font())
            elided_text = font_metrics.elidedText(convert_format, Qt.ElideRight, 110)
            action = QAction(elided_text, self.convertor_button)
            action.triggered.connect(lambda _, f=convert_format: self.set_convertor(f))
            self.convert_menu.addAction(action)

        self.convertor_button.clicked.connect(self.show_convert_menu)
        self.autoscroll_toggle.stateChanged.connect(self.set_autoscroll)

    @staticmethod
    def set_autoscroll(autoscroll):
        profile_manager.current_profile.autoscroll = bool(autoscroll)

    def set_convertor(self, convert_format):
        self.convertor_button.setText(convert_format)
        profile_manager.current_profile.convertor = convert_format

    def create_topic(self):
        if profile_manager.current_profile.is_default == 'True':
            self.notification_signal.emit(
                'You can\'t add a topic. You need to create or switch the profile',
                Result.FAILURE,
            )
            return None
        self.show_create_topic_dialog()

    def get_command_text(self):
        return self.command_field.toPlainText()

    def display_message_from_receiver_list(self, item):
        if item is None:
            return
        payload = item.data(Qt.UserRole)[0]
        self.receiver_text_edit.setPlainText(payload)

    def set_clipboard_messages(self, *, new: bool = False):
        clipboard_messages = {} if new else profile_manager.current_profile.clipboard

        self.clipboard_list.clear()

        for message_name, message_text in clipboard_messages.items():
            name_index = message_name.find('_id_starts_here_')
            item = QListWidgetItem()
            item.setText(message_name[:name_index])
            item.setData(Qt.UserRole, [message_text, message_name])
            self.clipboard_list.addItem(item)

    def display_message_in_command_field(self, item):
        command = item.data(Qt.UserRole)
        self.command_field.setPlainText(command[0])

    def save_message_to_clipboard(self, message_name: str, message_text: str):
        msg_id = profile_manager.current_profile.add_clipboard(
            message_name, message_text
        )
        item = QListWidgetItem()
        item.setText(message_name)
        item.setData(Qt.UserRole, [message_text, msg_id])
        self.clipboard_list.addItem(item)
        self.clipboard_list.setCurrentItem(item)

    def find_item_by_id(self, msg_id: str):
        for i in range(self.clipboard_list.count()):
            item = self.clipboard_list.item(i)
            item_data = item.data(Qt.UserRole)
            if item_data:
                if msg_id == item_data[1]:
                    return item
        return None

    def save_editing_message(
        self, start_data: list, msg_id, message_name: str, message_text: str
    ):
        new_data = profile_manager.current_profile.edit_clipboard(
            start_data, msg_id, message_name, message_text
        )
        item = self.find_item_by_id(msg_id)
        item.setText(new_data[1][0])
        item.setData(Qt.UserRole, [new_data[0], new_data[1][1]])
        self.clipboard_list.setCurrentItem(item)
        self.notification_signal.emit('Saved', Result.SUCCESS)

    def show_clipboard_dialog(self):
        return ClipboardDialog(self.save_message_to_clipboard, self).exec_()

    def show_clipboard_dialog_with_settings(self, name, message):
        ClipboardEditDialog(self.save_editing_message, [name, message], self).exec_()

    def save_and_subscribe_topic(self, _, topic_settings: dict, __):
        topic = profile_manager.current_profile.add_topic(topic_settings)
        self.tags_widget.add_tag(topic)
        if self.connector.is_connected:
            self.connector.subscribe(topic)
            self.notification_signal.emit('Created and subscribed successfully!', Result.SUCCESS)
        else:
            self.notification_signal.emit('Created successfully!', Result.SUCCESS)

    @staticmethod
    def save_topic(topic: Topic, new_settings: dict, tag_dict: dict):
        topic.set_fields_from_dict(new_settings)
        tag_dict['label'].setText(topic.get_name())
        if color := topic.color:
            tag_dict['frame'].setStyleSheet(
                tag_dict['frame'].styleSheet()
                + f'QFrame {{border-left: 2px solid {color};}} QFrame:hover {{border-left: 2px solid {color};}}'
            )

    def delete_topic(self, topic):
        self.tags_widget.remove_tag_by_address(topic.address)
        profile_manager.current_profile.delete_topic(topic)
        self.unsubscribe_topic(topic)

    def show_create_topic_dialog(self):
        TopicDialog(self.save_and_subscribe_topic, self).exec_()

    def show_edit_topic_dialog(self, topic, tag_dict):
        TopicDialog(self.save_topic, self, topic, tag_dict, self.delete_topic).exec_()

    def clear_list_and_message(self):
        self.receiver_text_edit.clear()
        self.receiver_list.clear()

    def get_selected_item(self):
        return self.clipboard_list.currentItem()

    def delete_clipboard_message(self, item):
        row = self.clipboard_list.row(item)
        self.clipboard_list.takeItem(row)
        profile_manager.current_profile.delete_clipboard(item.text())
