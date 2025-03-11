from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QFontMetrics, QIcon
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QAction,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QListWidget,
    QPushButton,
    QScrollBar,
    QSizePolicy,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from settings.profile_manager import profile_manager
from settings.topic import Topic
from UI import styles
from UI.icons.icons import EDIT_ICON
from UI.interface_utils import (
    Spacer,
    create_button,
    create_expand_button,
    create_frame,
    create_layout,
    create_list,
    create_spacer,
    deselect_tag,
    select_tag,
    set_topic_color,
)
from UI.styles import (
    ADD_TAG,
    CLIPBOARD_LIST,
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
            QHBoxLayout, [-1, 15, 10, 19], 0, out_layout=self.clear_frame
        )
        self.clear_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        self.clear_button = create_button(
            'clear', self.clear_frame, max_size=[50, 21], add_layout=self.clear_layout
        )

        self.receiver_list = create_list(
            self, styles.RECEIVER_LIST, self.main_right_layout
        )
        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet(styles.SCROLLBAR)
        self.receiver_list.setVerticalScrollBar(scroll_bar)

        self.filter_frame = create_frame(
            self,
            FILTER_FRAME,
            add_layout=self.main_right_layout,
        )
        self.message_formating = create_layout(
            QHBoxLayout, [12, 5, 0, 5], 0, out_layout=self.filter_frame
        )

        self.convertor_button, menu, show_menu = create_expand_button(
            'JSON',
            self.filter_frame,
            min_size=[100, 25],
            max_size=[100, 25],
            style=styles.PICKER_BUTTON,
            add_layout=self.message_formating,
        )

        for format in ('JSON', 'NotJSON'):
            font_metrics = QFontMetrics(self.convertor_button.font())
            elided_text = font_metrics.elidedText(
                format, Qt.ElideRight, 110
            )  # todo what is this

            action = QAction(elided_text, self.convertor_button)
            action.triggered.connect(lambda _, f=format: self.set_convertor(format))
            menu.addAction(action)

        self.convertor_button.clicked.connect(show_menu)

        self.message_formating.addItem(create_spacer(Spacer.HORIZONTAL))

        self.all_button = create_button(
            'All',
            self.filter_frame,
            min_size=[40, 23],
            max_size=[80, 23],
            style=styles.FILTER_BUTTON_2,
            add_layout=self.message_formating,
        )
        self.divider_1 = create_button(
            '',
            self.filter_frame,
            min_size=[1, 17],
            max_size=[1, 17],
            style=styles.DIVIDER,
            add_layout=self.message_formating,
        )

        self.received_button = create_button(
            'Received',
            self.filter_frame,
            min_size=[80, 23],
            max_size=[80, 23],
            style=styles.FILTER_BUTTON_2,
            add_layout=self.message_formating,
        )

        self.divider_2 = create_button(
            '',
            self.filter_frame,
            min_size=[1, 17],
            max_size=[1, 17],
            style=styles.DIVIDER,
            add_layout=self.message_formating,
        )

        self.published_button = create_button(
            'Published',
            self.filter_frame,
            min_size=[80, 23],
            max_size=[85, 23],
            style=styles.FILTER_BUTTON_1,
            add_layout=self.message_formating,
        )

        self.receiver_text_edit = QTextEdit(self)
        self.receiver_text_edit.setStyleSheet(RECEIVER_TEXT)
        self.receiver_text_edit.setReadOnly(True)
        self.receiver_text_edit.setFrameShape(QFrame.NoFrame)
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

        self.clipboard_list = QListWidget(self.main_left_layout)  # todo: refactor
        self.clipboard_list.setDragEnabled(True)
        self.clipboard_list.setAcceptDrops(True)
        self.clipboard_list.setDragDropMode(QAbstractItemView.InternalMove)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clipboard_list.sizePolicy().hasHeightForWidth()
        )
        self.clipboard_list.setSizePolicy(sizePolicy)
        self.clipboard_list.setMinimumSize(QtCore.QSize(220, 0))
        self.clipboard_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clipboard_list.setStyleSheet(CLIPBOARD_LIST)
        self.clipboard_list.setFrameShape(QFrame.NoFrame)
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

    def set_convertor(self, f):
        self.convertor_button.setText(f)


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
            '', self, style=ADD_TAG, min_size=30, max_size=30
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
        tag_label.setStyleSheet("QLabel {color: rgb(186, 189, 182); border: none}")
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
