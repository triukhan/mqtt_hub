from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from GUI import styles
from GUI.interface_utils import create_button, create_frame, create_layout, create_list

vertical_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
horizontal_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)


class MainTab(QWidget):
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
        self.clear_layout.addItem(vertical_spacer)
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

        self.message_formating.addItem(vertical_spacer)

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
        self.verticalLayout_3 = QVBoxLayout(self.main_left_layout)
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.publisher_head_frame = QFrame(self.main_left_layout)
        self.publisher_head_frame.setStyleSheet(
            "QFrame {background-color: rgb(35, 35, 35)}"
        )
        self.horizontalLayout_5 = QHBoxLayout(self.publisher_head_frame)
        self.horizontalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_5.setSpacing(20)
        self.delete_button = QPushButton(self.publisher_head_frame)
        self.delete_button.setMinimumSize(QtCore.QSize(0, 25))
        self.delete_button.setMaximumSize(QtCore.QSize(16777215, 25))
        self.delete_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(140, 50, 0);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-radius: 5;\n"
            "   padding: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: 1px solid rgb(70, 70, 70); \n"
            "}"
        )
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_5.addWidget(self.delete_button)
        self.add_clipboard_button = QPushButton(self.publisher_head_frame)
        self.add_clipboard_button.setMinimumSize(QtCore.QSize(0, 25))
        self.add_clipboard_button.setMaximumSize(QtCore.QSize(16777215, 25))
        self.add_clipboard_button.setStyleSheet(styles.APP_BUTTON)
        self.add_clipboard_button.setObjectName("add_clipboard_button")
        self.horizontalLayout_5.addWidget(self.add_clipboard_button)
        self.qos_layout = QHBoxLayout()
        self.qos_layout.setSpacing(0)
        self.qos_layout.setObjectName("qos_layout")
        self.qos_button = QPushButton(self.publisher_head_frame)
        self.qos_button.setMinimumSize(QtCore.QSize(0, 25))
        self.qos_button.setMaximumSize(QtCore.QSize(50, 25))
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
        self.qos_button.setObjectName("qos_button")
        self.qos_layout.addWidget(self.qos_button)
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
        self.publish_button = QPushButton(self.publisher_head_frame)
        self.publish_button.setMinimumSize(QtCore.QSize(0, 25))
        self.publish_button.setMaximumSize(QtCore.QSize(16777215, 25))
        self.publish_button.setStyleSheet(styles.APP_BUTTON)
        self.horizontalLayout_5.addWidget(self.publish_button)
        self.verticalLayout_3.addWidget(self.publisher_head_frame)
        self.clipboard_layout = QHBoxLayout()
        self.clipboard_layout.setContentsMargins(-1, -1, 1, -1)
        self.clipboard_layout.setSpacing(0)
        self.command_list = QListWidget(self.main_left_layout)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.command_list.sizePolicy().hasHeightForWidth())
        self.command_list.setSizePolicy(sizePolicy)
        self.command_list.setMinimumSize(QtCore.QSize(220, 0))
        self.command_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.command_list.setFont(font)
        self.command_list.setStyleSheet(
            "QListView {\n"
            "    border-top: 1px solid rgb(50, 50, 50); \n"
            "    border-bottom: 1px solid rgb(50, 50, 50); \n"
            "    background-color: rgb(35, 35, 35);\n"
            "}\n"
            "\n"
            "QListView::item {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(45, 45, 45);\n"
            "}\n"
            "\n"
            "QListView::item:selected {\n"
            "    background-color: rgb(40, 40, 40);\n"
            "    color: #FFF; \n"
            "    border-color: rgb(114, 159, 207);\n"
            "}"
        )
        self.command_list.setFrameShape(QFrame.NoFrame)
        self.command_list.setObjectName("command_list")
        item = QListWidgetItem()
        self.command_list.addItem(item)
        self.clipboard_layout.addWidget(self.command_list)
        self.comand_field = QTextEdit(self.main_left_layout)
        self.comand_field.setStyleSheet(
            "QTextEdit {\n"
            " background-color: rgb(26, 26, 27);\n"
            " color: rgb(186, 189, 182);\n"
            "    border: 1px solid rgb(50, 50, 50); \n"
            "}\n"
            ""
        )
        self.comand_field.setFrameShape(QFrame.NoFrame)
        self.comand_field.setObjectName("comand_field")
        self.clipboard_layout.addWidget(self.comand_field)
        self.clipboard_layout.setStretch(0, 1)
        self.clipboard_layout.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.clipboard_layout)
        self.gridLayout_2.addWidget(self.main_left_layout, 0, 0, 1, 1)
