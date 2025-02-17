from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLayout,
    QListWidget,
    QPushButton,
    QScrollBar,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from GUI import styles
from GUI.interface_utils import (
    create_button,
    create_frame,
    create_layout,
    create_list,
    horizontal_spacer,
)


class MainTabUI(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout_2 = create_layout(QGridLayout, [0, 0, 0, 0], 0, out_layout=self)
        self.main_right_layout = create_layout(QVBoxLayout, [0, -1, 0, 0], 0)

        # clear
        self.clear_frame = create_frame(
            self,
            'QFrame {background-color: rgb(35, 35, 35)}',
            add_layout=self.main_right_layout,
        )
        self.clear_layout = create_layout(
            QHBoxLayout, [-1, 15, 10, 19], 0, out_layout=self.clear_frame
        )
        self.clear_layout.addItem(horizontal_spacer)
        self.clear_button = create_button(
            'clear', self.clear_frame, max_size=(50, 21), add_layout=self.clear_layout
        )

        self.receiver_list = create_list(
            self, styles.RECEIVER_LIST, self.main_right_layout
        )
        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet(styles.SCROLLBAR)
        self.receiver_list.setVerticalScrollBar(scroll_bar)

        self.filter_frame = create_frame(
            self,
            'QFrame {border-top: 1px solid rgb(50, 50, 50); border-bottom: 1px solid rgb(50, 50, 50);'
            'background-color: rgb(35, 35, 35)}',
            add_layout=self.main_right_layout,
        )
        self.message_formating = create_layout(
            QHBoxLayout, [12, 5, 0, 5], 0, out_layout=self.filter_frame
        )

        self.convertor_button = create_button(
            'JSON',
            self.filter_frame,
            min_size=(100, 25),
            max_size=(100, 25),
            style=styles.PICKER_BUTTON,
            add_layout=self.message_formating,
        )

        self.convertor_button.setIcon(QIcon('GUI/icons/expand-profile-icon.png'))
        self.convertor_button.setIconSize(QSize(24, 24))
        self.convertor_button.setLayoutDirection(Qt.RightToLeft)

        self.message_formating.addItem(horizontal_spacer)

        self.all_button = create_button(
            'All',
            self.filter_frame,
            min_size=(40, 23),
            max_size=(80, 23),
            style=styles.FILTER_BUTTON_2,
            add_layout=self.message_formating,
        )
        self.divider_1 = create_button(
            '',
            self.filter_frame,
            min_size=(1, 17),
            max_size=(1, 17),
            style=styles.DIVIDER,
            add_layout=self.message_formating,
        )

        self.received_button = create_button(
            'Received',
            self.filter_frame,
            min_size=(80, 23),
            max_size=(80, 23),
            style=styles.FILTER_BUTTON_2,
            add_layout=self.message_formating,
        )

        self.divider_2 = create_button(
            '',
            self.filter_frame,
            min_size=(1, 17),
            max_size=(1, 17),
            style=styles.DIVIDER,
            add_layout=self.message_formating,
        )

        self.published_button = create_button(
            'Published',
            self.filter_frame,
            min_size=(80, 23),
            max_size=(85, 23),
            style=styles.FILTER_BUTTON_1,
            add_layout=self.message_formating,
        )

        self.receiver_text_edit = QTextEdit(self)
        self.receiver_text_edit.setStyleSheet('QTextEdit {color: rgb(186, 189, 182);}')
        self.receiver_text_edit.setFrameShape(QFrame.NoFrame)
        self.main_right_layout.addWidget(self.receiver_text_edit)

        self.gridLayout_2.addLayout(self.main_right_layout, 0, 1, 1, 1)

        self.main_left_layout = QFrame(self)

        self.verticalLayout_3 = create_layout(
            QVBoxLayout, margins=0, out_layout=self.main_left_layout
        )

        self.publisher_head_frame = create_frame(
            self.main_left_layout, style='QFrame {background-color: rgb(35, 35, 35)}'
        )

        self.horizontalLayout_5 = create_layout(
            QHBoxLayout, 15, 20, out_layout=self.publisher_head_frame
        )

        self.delete_button = create_button(
            'Delete',
            self.publisher_head_frame,
            min_size=(0, 25),
            max_size=(100, 25),
            add_layout=self.horizontalLayout_5,
        )
        self.delete_button.setStyleSheet(
            "QPushButton {color: rgb(140, 50, 0); background-color: rgb(35, 35, 35); border: 1px solid "
            "rgb(50, 50, 50); border-radius: 5; padding: 5px; } QPushButton:hover {border: 1px solid rgb(70, 70, 70)}"
        )

        self.add_clipboard_button = create_button(
            'Add to Clipboard',
            self.publisher_head_frame,
            min_size=(0, 25),
            max_size=(150, 25),
            style=styles.APP_BUTTON,
            add_layout=self.horizontalLayout_5,
        )

        self.qos_button = create_button(
            'Qos 0',
            self.publisher_head_frame,
            styles.PICKER_BUTTON,
            min_size=(0, 25),
            max_size=(80, 25),
            add_layout=self.horizontalLayout_5,
        )
        self.qos_button.setIcon(QIcon('GUI/icons/expand-profile-icon.png'))
        self.qos_button.setIconSize(QSize(24, 24))
        self.qos_button.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_5.addWidget(self.qos_button)

        self.publish_button = create_button(
            'Publish',
            self.publisher_head_frame,
            min_size=(0, 25),
            max_size=(150, 25),
            add_layout=self.horizontalLayout_5,
        )

        self.verticalLayout_3.addWidget(self.publisher_head_frame)
        self.clipboard_layout = create_layout(QHBoxLayout, [-1, -1, 1, -1])

        self.clipboard_list = QListWidget(self.main_left_layout)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clipboard_list.sizePolicy().hasHeightForWidth()
        )
        self.clipboard_list.setSizePolicy(sizePolicy)
        self.clipboard_list.setMinimumSize(QtCore.QSize(220, 0))
        self.clipboard_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clipboard_list.setStyleSheet(
            'QListView {border-top: 1px solid rgb(50, 50, 50); border-bottom: 1px solid rgb(50, 50, 50);'
            'background-color: rgb(35, 35, 35);} QListView::item {color: rgb(186, 189, 182); background-color: '
            'rgb(45, 45, 45);} QListView::item:selected {background-color: rgb(40, 40, 40); color: #FFF;'
            'border-color: rgb(114, 159, 207);}'
        )
        self.clipboard_list.setFrameShape(QFrame.NoFrame)
        self.clipboard_layout.addWidget(self.clipboard_list)
        self.command_field = QTextEdit(self.main_left_layout)
        self.command_field.setStyleSheet(
            'QTextEdit {background-color: rgb(26, 26, 27); color: rgb(186, 189, 182); border: 1px solid rgb(50, 50, 50);}'
        )
        self.command_field.setFrameShape(QFrame.NoFrame)
        self.clipboard_layout.addWidget(self.command_field)
        self.clipboard_layout.setStretch(0, 1)
        self.clipboard_layout.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.clipboard_layout)
        self.bottom_frame = QWidget(self.main_left_layout)
        self.bottom_frame.setFixedHeight(0)
        self.tags_widget = TagsWidget(self.bottom_frame)
        self.add_button = self.tags_widget.add_button
        self.verticalLayout_3.addWidget(self.tags_widget)
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
                last_item.setGeometry(
                    QRect(QPoint(x - 55, y - 5), last_item.sizeHint())
                )


class TagsWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(100)
        self.setStyleSheet("QFrame {background: rgb(35, 35, 35); border: none;}")
        self.setContentsMargins(15, 15, 15, 15)

        self.tags_layout = FlowLayout(self, spacing=20)
        self.setLayout(self.tags_layout)

        add_button = (
            'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-radius: 5; '
            'padding: 5px; border-image: url(GUI/icons/plus-icon.png) 0 0 0 0 stretch stretch;}}'
            'QPushButton:hover {background-color: rgb(45, 45, 45)}'
        )
        self.add_button = create_button('', self, add_button, min_size=30, max_size=30)
        self.tags_layout.addWidget(self.add_button)

    def add_tag(self, tag_text: str = ''):
        tag_button_style = (
            'QPushButton {color: rgb(186, 189, 182); background-color: rgb(45, 45, 45); border-radius: 8; padding: 5px}'
            'QPushButton:hover {border: 1px solid rgb(70, 70, 70);}'
        )
        tag_button = create_button(
            tag_text or f"Tag {len(self.tags_layout.item_list)}",
            self,
            tag_button_style,
            max_size=(112, 30),
        )
        tag_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        tag_button.clicked.connect(lambda: self.remove_tag(tag_button))

        self.tags_layout.insertWidget(self.tags_layout.count() - 1, tag_button)

    def remove_tag(self, button):
        self.tags_layout.removeWidget(button)
