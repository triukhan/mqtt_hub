from PyQt5.QtCore import QPoint, QRect, QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from settings.profile_manager import profile_manager
from settings.topic import Topic
from UI import styles
from UI.custom_widgets.clipboard_list import ClipboardListWidget
from UI.icons.icons import EDIT_ICON
from UI.interface_utils import (
    Spacer,
    create_button,
    create_expand_button,
    create_frame,
    create_label,
    create_layout,
    create_list,
    create_scroll_bar,
    create_spacer,
    create_toggle,
    deselect_tag,
    select_tag,
    set_topic_color,
)
from UI.styles import (
    ADD_TAG,
    CLEAR_BUTTON,
    COMMAND_FIELD,
    DELETE_BUTTON,
    EDIT_TAG,
    FILTER_FRAME,
    FRAME_COLOR,
    RECEIVER_TEXT,
    TAG,
)


class MainTabUI(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout_2 = create_layout(QGridLayout, [0, 0, 0, 0], 0, out_layout=self)
        self.main_right_layout = create_layout(QVBoxLayout, [0, -1, 0, 0], 0)

        self.clear_frame = create_frame(
            self,
            FRAME_COLOR,
            add_layout=self.main_right_layout,
        )
        self.clear_layout = create_layout(
            QHBoxLayout, [10, 12, 10, 10], 0, out_layout=self.clear_frame
        )

        self.autoscroll_toggle = create_toggle(self.clear_layout)
        self.autoscroll_label = create_label(
            'Autoscroll',
            self.clear_frame,
            self.clear_layout,
            style=styles.LABEL + 'QLabel {margin-bottom: 2px}',
        )
        self.clear_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        font = QFont()
        font.setPointSize(10)
        self.clear_button = create_button(
            'clear',
            self.clear_frame,
            max_size=[50, 18],
            add_layout=self.clear_layout,
            style=CLEAR_BUTTON,
            font=font,
        )

        self.receiver_list = create_list(
            self, styles.RECEIVER_LIST, self.main_right_layout
        )
        create_scroll_bar(self, self.receiver_list)

        self.filter_frame = create_frame(
            self,
            FILTER_FRAME,
            add_layout=self.main_right_layout,
        )
        self.message_formating = create_layout(
            QHBoxLayout, [12, 5, 0, 5], 0, out_layout=self.filter_frame
        )

        self.convertor_button, self.convert_menu, self.show_convert_menu = (
            create_expand_button(
                profile_manager.current_profile.convertor,
                self.filter_frame,
                min_size=[100, 25],
                max_size=[100, 25],
                style=styles.PICKER_BUTTON,
                add_layout=self.message_formating,
            )
        )

        self.message_formating.addItem(create_spacer(Spacer.HORIZONTAL))

        self.select_label = create_label(
            'Select Message  ',
            self.filter_frame,
            min_size=[110, 23],
            max_size=[110, 23],
            add_layout=self.message_formating,
        )

        self.select_toggle = create_toggle(self.message_formating)

        self.receiver_text_edit = QTextEdit(self)  # todo
        self.receiver_text_edit.setStyleSheet(RECEIVER_TEXT)
        self.receiver_text_edit.setReadOnly(True)
        self.receiver_text_edit.setFrameShape(QFrame.NoFrame)
        create_scroll_bar(self, self.receiver_text_edit)

        self.main_right_layout.addWidget(self.receiver_text_edit)

        self.gridLayout_2.addLayout(self.main_right_layout, 0, 1, 1, 1)

        self.main_left_layout = QFrame(self)

        self.verticalLayout_3 = create_layout(
            QVBoxLayout, margins=0, out_layout=self.main_left_layout
        )

        self.publisher_head_frame = create_frame(
            self.main_left_layout, style=FRAME_COLOR
        )

        self.horizontalLayout_5 = create_layout(
            QHBoxLayout, 15, 20, out_layout=self.publisher_head_frame
        )

        self.delete_button = create_button(
            'Delete',
            self.publisher_head_frame,
            min_size=[0, 25],
            max_size=[100, 25],
            add_layout=self.horizontalLayout_5,
        )
        self.delete_button.setStyleSheet(DELETE_BUTTON)

        self.add_clipboard_button = create_button(
            'Add to Clipboard',
            self.publisher_head_frame,
            [0, 25],
            [150, 25],
            self.horizontalLayout_5,
            style=styles.APP_BUTTON,
        )

        self.publish_button = create_button(
            'Publish',
            self.publisher_head_frame,
            min_size=[0, 25],
            max_size=[150, 25],
            add_layout=self.horizontalLayout_5,
        )

        self.verticalLayout_3.addWidget(self.publisher_head_frame)
        self.clipboard_layout = create_layout(QHBoxLayout, [-1, -1, 1, -1])

        self.clipboard_list = ClipboardListWidget(self.main_left_layout)
        self.clipboard_layout.addWidget(self.clipboard_list)

        self.command_field = QTextEdit(self.main_left_layout)
        self.command_field.setStyleSheet(COMMAND_FIELD)
        self.command_field.setFrameShape(QFrame.NoFrame)
        self.clipboard_layout.addWidget(self.command_field)
        self.clipboard_layout.setStretch(0, 1)
        self.clipboard_layout.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.clipboard_layout)
        self.bottom_frame = QWidget(self.main_left_layout)
        self.bottom_frame.setFixedHeight(0)
        self.gridLayout_2.addWidget(self.main_left_layout, 0, 0, 1, 1)


class FlowLayout(QLayout):
    def __init__(self, parent=None, spacing=5):
        super().__init__(parent)
        self.item_list = []
        self._spacing = spacing

    def addItem(self, item):
        self.item_list.append(item)
        self.invalidate()

    def itemAt(self, index):
        if index < 0 or index >= len(self.item_list):
            return None
        return self.item_list[index]

    def insertWidget(self, index, widget):
        self.addWidget(widget)
        self.item_list.insert(index, self.item_list.pop(-1))
        self.invalidate()

    def removeWidget(self, widget):
        if widget in [item.widget() for item in self.item_list]:
            widget.deleteLater()
            self.item_list = [
                item for item in self.item_list if item.widget() != widget
            ]
            self.invalidate()

    def count(self):
        return len(self.item_list)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize(0, 0)
        for item in self.item_list:
            size = size.expandedTo(item.sizeHint())
        return size + QSize(2 * self._spacing, 2 * self._spacing)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        x, y, rowHeight = rect.x(), rect.y(), 0
        for item in self.item_list:
            next_x = x + item.sizeHint().width() + self._spacing
            if next_x > rect.right() and rowHeight > 0:
                x = rect.x()
                y += rowHeight + self._spacing
                next_x = x + item.sizeHint().width() + self._spacing
                rowHeight = 0
            item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
            x = next_x
            rowHeight = max(rowHeight, item.sizeHint().height())

        if self.item_list:
            last_item = self.item_list[-1]
            if (
                isinstance(last_item.widget(), QPushButton)
                and last_item.widget().text() == ''
            ):
                last_item.setGeometry(QRect(QPoint(x - 40, y), last_item.sizeHint()))


class TagsWidget(QFrame):
    def __init__(self, parent=None, edit_method=None):
        super().__init__(parent)
        self.edit_method = edit_method
        self.selected_tag = None

        self.setFixedHeight(100)
        self.setStyleSheet(FRAME_COLOR)
        self.setContentsMargins(10, 10, 0, 0)

        self.tags_layout = FlowLayout(self, spacing=10)
        self.setLayout(self.tags_layout)

        self.add_button = create_button(
            '', self, style=ADD_TAG, min_size=30, max_size=30, border=False
        )
        self.add_button.setProperty('add_button', True)
        self.tags_layout.addWidget(self.add_button)

    def add_tag(self, topic: Topic):
        tag = create_frame(self, TAG)
        set_topic_color(topic, tag)
        tag.setFixedSize(115, 30)
        tag_layout = create_layout(QHBoxLayout, 0, 0, tag)

        tag_label = QLabel(topic.get_name(), tag)  # todo: create_label
        tag_label.setFixedWidth(90)
        tag_label.setStyleSheet('QLabel {color: rgb(186, 189, 182); border: none}')
        tag_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )

        icon_button = QToolButton(tag)
        icon_button.setIcon(QIcon(EDIT_ICON))
        icon_button.setIconSize(QSize(32, 32))
        icon_button.setFixedSize(18, 18)
        icon_button.setStyleSheet(EDIT_TAG)
        icon_button.clicked.connect(
            lambda: self.edit_method(topic, {'frame': tag, 'label': tag_label})
        )

        tag_layout.addWidget(tag_label)
        tag_layout.addWidget(icon_button)
        tag.setLayout(tag_layout)
        tag.setProperty('address', topic.address)

        tag.mousePressEvent = lambda event: self.select_tag(tag, topic)
        self.tags_layout.insertWidget(self.tags_layout.count() - 1, tag)

    def select_tag(self, tag, topic):
        if self.selected_tag:
            deselect_tag(self.selected_tag)

        self.selected_tag = tag
        select_tag(self.selected_tag)
        profile_manager.topic_to_publish = topic

    def remove_tag(self, tag):
        self.tags_layout.removeWidget(tag)

    def clear_tags(self):
        for i in range(self.tags_layout.count() - 1, -1, -1):
            item = self.tags_layout.itemAt(i)
            if item:
                tag_frame = item.widget()
                if tag_frame.property('add_button'):
                    continue
                self.remove_tag(tag_frame)

    def find_tag_by_address(self, address):
        for i in range(self.tags_layout.count() - 1, -1, -1):
            item = self.tags_layout.itemAt(i)
            if item:
                tag_frame = item.widget()
                if tag_frame.property('address') == address:
                    return tag_frame

    def remove_tag_by_address(self, address):
        tag = self.find_tag_by_address(address)
        self.remove_tag(tag)
        profile_manager.topic_to_publish = None
        self.selected_tag = None
