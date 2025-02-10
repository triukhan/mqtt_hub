from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, QRect, QSize
from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
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
            'clear', self.clear_frame, add_layout=self.clear_layout
        )

        self.receiver_list = create_list(self, add_layout=self.main_right_layout)
        item = QListWidgetItem()
        self.receiver_list.addItem(item)
        item = QListWidgetItem()
        self.receiver_list.addItem(item)

        self.filter_frame = create_frame(
            self,
            'QFrame {border-top: 1px solid rgb(50, 50, 50); border-bottom: 1px solid rgb(50, 50, 50);'
            'background-color: rgb(35, 35, 35)}',
            add_layout=self.main_right_layout,
        )
        self.message_formating = create_layout(
            QHBoxLayout, [12, 5, 0, 5], 0, out_layout=self.filter_frame
        )

        style = (
            'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border:'
            '1px solid rgb(50, 50, 50); border-right: 0px; border-top-left-radius: 5; border-bottom-left-radius: 5;'
            'padding: 5px} QPushButton:hover {border: 1px solid rgb(70, 70, 70); border-right: 0px}'
        )
        self.convertor_button = create_button(
            'MsgPack',
            self.filter_frame,
            min_size=(70, 25),
            max_size=(70, 25),
            style=style,
            add_layout=self.message_formating,
        )
        style = (
            'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border: 1px solid '
            'rgb(50, 50, 50); border-left: 0px; border-top-right-radius: 5; border-bottom-right-radius: 5;'
            'padding: 5px} QPushButton:hover {border: 1px solid rgb(70, 70, 70); border-left: 0px}'
        )
        self.convertor_picker_button = create_button(
            '',
            self.filter_frame,
            min_size=(25, 25),
            max_size=(25, 25),
            style=style,
            add_layout=self.message_formating,
        )

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
        self.receiver_text_edit.setStyleSheet(styles.FILTER_BUTTON_1)
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

        self.qos_layout = create_layout(QHBoxLayout)

        self.qos_button = create_button(
            'Qos',
            self.publisher_head_frame,
            min_size=(0, 25),
            max_size=(50, 25),
            add_layout=self.qos_layout,
        )
        self.qos_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-right: 0px; \n"
            "   border-top-left-radius: 5;\n"
            "   border-bottom-left-radius: 5;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: 1px solid rgb(70, 70, 70); \n"
            "   border-right: 0px; \n"
            "}"
        )
        self.qos_picker_button = QPushButton(self.publisher_head_frame)
        self.qos_picker_button.setMinimumSize(QtCore.QSize(25, 25))
        self.qos_picker_button.setMaximumSize(QtCore.QSize(25, 25))
        self.qos_picker_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-left: 0px; \n"
            "   border-top-right-radius: 5;\n"
            "   border-bottom-right-radius: 5;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: 1px solid rgb(70, 70, 70);\n"
            "   border-left: 0px;  \n"
            "}"
        )
        self.qos_picker_button.setObjectName("qos_picker_button")
        self.qos_layout.addWidget(self.qos_picker_button)
        self.horizontalLayout_5.addLayout(self.qos_layout)

        self.publish_button = create_button(
            'Publish',
            self.publisher_head_frame,
            min_size=(0, 25),
            max_size=(150, 25),
            add_layout=self.horizontalLayout_5,
        )

        self.verticalLayout_3.addWidget(self.publisher_head_frame)
        self.clipboard_layout = create_layout(QHBoxLayout, [-1, -1, 1, -1])

        self.command_list = QListWidget(self.main_left_layout)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.command_list.sizePolicy().hasHeightForWidth())
        self.command_list.setSizePolicy(sizePolicy)
        self.command_list.setMinimumSize(QtCore.QSize(220, 0))
        self.command_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.command_list.setStyleSheet(
            'QListView {border-top: 1px solid rgb(50, 50, 50); border-bottom: 1px solid rgb(50, 50, 50);'
            'background-color: rgb(35, 35, 35);} QListView::item {color: rgb(186, 189, 182); background-color: '
            'rgb(45, 45, 45);} QListView::item:selected {background-color: rgb(40, 40, 40); color: #FFF;'
            'border-color: rgb(114, 159, 207);}'
        )
        self.command_list.setFrameShape(QFrame.NoFrame)
        item = QListWidgetItem()
        self.command_list.addItem(item)
        self.clipboard_layout.addWidget(self.command_list)
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
                and last_item.widget().text() == '+'
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

        self.add_button = create_button('+', self, min_size=30, max_size=30)
        self.tags_layout.addWidget(self.add_button)

    def add_tag(self, tag_text: str = ''):
        tag_button = create_button(
            tag_text or f"Tag {len(self.tags_layout.item_list)}",
            self,
            max_size=(112, 30),
        )
        tag_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        tag_button.clicked.connect(lambda: self.remove_tag(tag_button))

        self.tags_layout.insertWidget(self.tags_layout.count() - 1, tag_button)

    def remove_tag(self, button):
        self.tags_layout.removeWidget(button)
