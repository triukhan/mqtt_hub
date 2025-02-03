from PyQt5 import QtCore, QtGui, QtWidgets

from GUI import styles
from GUI.info_tab import InfoTab
from GUI.plus_tab import PlusTab


class MqttHubUi(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 904)
        MainWindow.setStyleSheet(
            "QFrame {\n" "    background-color: rgb(35, 35, 35);\n" "}\n" ""
        )
        self.main_window = QtWidgets.QWidget(MainWindow)
        self.main_window.setStyleSheet(
            "QWidget {\n" "    background-color: rgb(30, 30, 30);\n" "}\n" ""
        )
        self.main_window.setObjectName("main_window")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_window)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.main_w = QtWidgets.QGridLayout()
        self.main_w.setSpacing(0)
        self.main_w.setObjectName("main_w")
        self.tab_layout = QtWidgets.QGridLayout()
        self.tab_layout.setSpacing(0)
        self.tab_layout.setObjectName("tab_layout")
        self.all_tabs = QtWidgets.QTabWidget(self.main_window)
        self.all_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.all_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.all_tabs.setElideMode(QtCore.Qt.ElideRight)
        self.all_tabs.setUsesScrollButtons(False)
        self.all_tabs.setTabsClosable(False)
        self.all_tabs.setMovable(False)
        self.all_tabs.setTabBarAutoHide(False)
        self.all_tabs.setObjectName("all_tabs")
        self.main_tab = QtWidgets.QWidget()
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_right_layout = QtWidgets.QVBoxLayout()
        self.main_right_layout.setContentsMargins(0, -1, 0, 0)
        self.main_right_layout.setSpacing(0)
        self.main_right_layout.setObjectName("main_right_layout")
        self.clear_frame = QtWidgets.QFrame(self.main_tab)
        self.clear_frame.setStyleSheet("QFrame{background-color: rgb(35, 35, 35);}")
        self.clear_frame.setObjectName("clear_frame")
        self.clear_layout = QtWidgets.QHBoxLayout(self.clear_frame)
        self.clear_layout.setContentsMargins(-1, 15, 10, 19)
        self.clear_layout.setSpacing(0)
        self.clear_layout.setObjectName("clear_layout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.clear_layout.addItem(spacerItem)
        self.clear_button = QtWidgets.QPushButton(self.clear_frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
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
        self.clear_button.setObjectName("clear_button")
        self.clear_layout.addWidget(self.clear_button)
        self.main_right_layout.addWidget(self.clear_frame)
        self.receiver_list = QtWidgets.QListWidget(self.main_tab)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.receiver_list.setFont(font)
        self.receiver_list.setStyleSheet(
            "QListView {\n"
            "    background-color: rgb(35, 35, 35);\n"
            "}\n"
            "QListView::item {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(45, 45, 45)\n"
            "}\n"
            "\n"
            "QListView::item:selected {\n"
            "    background-color: rgb(40, 40, 40);\n"
            "    color: #FFF; \n"
            "    border-color: rgb(114, 159, 207);\n"
            "}"
        )
        self.receiver_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.receiver_list.setObjectName("receiver_list")
        item = QtWidgets.QListWidgetItem()
        self.receiver_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.receiver_list.addItem(item)
        self.main_right_layout.addWidget(self.receiver_list)
        self.filter_frame = QtWidgets.QFrame(self.main_tab)
        self.filter_frame.setStyleSheet(
            "QFrame {\n"
            "    border-top: 1px solid rgb(50, 50, 50); \n"
            "    border-bottom: 1px solid rgb(50, 50, 50); \n"
            "    background-color: rgb(35, 35, 35);\n"
            "}\n"
            ""
        )
        self.filter_frame.setObjectName("filter_frame")
        self.message_formating = QtWidgets.QHBoxLayout(self.filter_frame)
        self.message_formating.setContentsMargins(12, 5, 0, 5)
        self.message_formating.setSpacing(0)
        self.message_formating.setObjectName("message_formating")
        self.convertor_button = QtWidgets.QPushButton(self.filter_frame)
        self.convertor_button.setMinimumSize(QtCore.QSize(70, 25))
        self.convertor_button.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.convertor_button.setFont(font)
        self.convertor_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-right: 0px; \n"
            "   border-top-left-radius: 5;\n"
            "   border-bottom-left-radius: 5;\n"
            "   padding: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: 1px solid rgb(70, 70, 70); \n"
            "   border-right: 0px; \n"
            "}"
        )
        self.convertor_button.setObjectName("convertor_button")
        self.message_formating.addWidget(self.convertor_button)
        self.convertor_picker_button = QtWidgets.QPushButton(self.filter_frame)
        self.convertor_picker_button.setMinimumSize(QtCore.QSize(25, 25))
        self.convertor_picker_button.setMaximumSize(QtCore.QSize(25, 25))
        self.convertor_picker_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-left: 0px; \n"
            "   border-top-right-radius: 5;\n"
            "   border-bottom-right-radius: 5;\n"
            "   padding: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: 1px solid rgb(70, 70, 70);\n"
            "   border-left: 0px;  \n"
            "}"
        )
        self.convertor_picker_button.setObjectName("convertor_picker_button")
        self.message_formating.addWidget(self.convertor_picker_button)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.message_formating.addItem(spacerItem1)
        self.all_button = QtWidgets.QPushButton(self.filter_frame)
        self.all_button.setMinimumSize(QtCore.QSize(40, 23))
        self.all_button.setMaximumSize(QtCore.QSize(80, 24))
        self.all_button.setFont(font)
        self.all_button.setStyleSheet(styles.FILTER_BUTTON)
        self.message_formating.addWidget(self.all_button)
        self.divider_1 = QtWidgets.QPushButton(self.filter_frame)
        self.divider_1.setMinimumSize(QtCore.QSize(1, 17))
        self.divider_1.setMaximumSize(QtCore.QSize(1, 17))
        self.divider_1.setStyleSheet(styles.DIVIDER)
        self.divider_1.setText("")
        self.message_formating.addWidget(self.divider_1)
        self.received_button = QtWidgets.QPushButton(self.filter_frame)
        self.received_button.setMinimumSize(QtCore.QSize(80, 23))
        self.received_button.setMaximumSize(QtCore.QSize(80, 24))
        self.received_button.setFont(font)
        self.received_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: 1px solid rgb(35, 35, 35); \n"
            "   padding: 5px;\n"
            "}"
        )
        self.message_formating.addWidget(self.received_button)
        self.divider_2 = QtWidgets.QPushButton(self.filter_frame)
        self.divider_2.setMinimumSize(QtCore.QSize(1, 17))
        self.divider_2.setMaximumSize(QtCore.QSize(1, 17))
        self.divider_2.setStyleSheet(styles.DIVIDER)
        self.divider_2.setText("")
        self.divider_2.setObjectName("divider_2")
        self.message_formating.addWidget(self.divider_2)
        self.published_button = QtWidgets.QPushButton(self.filter_frame)
        self.published_button.setMinimumSize(QtCore.QSize(80, 23))
        self.published_button.setMaximumSize(QtCore.QSize(85, 23))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.published_button.setFont(font)
        self.published_button.setStyleSheet(styles.FILTER_BUTTON)
        self.message_formating.addWidget(self.published_button)
        self.main_right_layout.addWidget(self.filter_frame)
        self.receiver_text_edit = QtWidgets.QTextEdit(self.main_tab)
        self.receiver_text_edit.setStyleSheet(styles.FILTER_BUTTON)
        self.receiver_text_edit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_right_layout.addWidget(self.receiver_text_edit)
        self.gridLayout_2.addLayout(self.main_right_layout, 0, 1, 1, 1)
        self.main_left_layout = QtWidgets.QFrame(self.main_tab)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_left_layout)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.publisher_head_frame = QtWidgets.QFrame(self.main_left_layout)
        self.publisher_head_frame.setStyleSheet(
            "QFrame {background-color: rgb(35, 35, 35)}"
        )
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.publisher_head_frame)
        self.horizontalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_5.setSpacing(20)
        self.delete_button = QtWidgets.QPushButton(self.publisher_head_frame)
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
        self.add_clipboard_button = QtWidgets.QPushButton(self.publisher_head_frame)
        self.add_clipboard_button.setMinimumSize(QtCore.QSize(0, 25))
        self.add_clipboard_button.setMaximumSize(QtCore.QSize(16777215, 25))
        self.add_clipboard_button.setStyleSheet(styles.APP_BUTTON)
        self.add_clipboard_button.setObjectName("add_clipboard_button")
        self.horizontalLayout_5.addWidget(self.add_clipboard_button)
        self.qos_layout = QtWidgets.QHBoxLayout()
        self.qos_layout.setSpacing(0)
        self.qos_layout.setObjectName("qos_layout")
        self.qos_button = QtWidgets.QPushButton(self.publisher_head_frame)
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
        self.qos_picker_button = QtWidgets.QPushButton(self.publisher_head_frame)
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
        self.publish_button = QtWidgets.QPushButton(self.publisher_head_frame)
        self.publish_button.setMinimumSize(QtCore.QSize(0, 25))
        self.publish_button.setMaximumSize(QtCore.QSize(16777215, 25))
        self.publish_button.setStyleSheet(styles.APP_BUTTON)
        self.horizontalLayout_5.addWidget(self.publish_button)
        self.verticalLayout_3.addWidget(self.publisher_head_frame)
        self.clipboard_layout = QtWidgets.QHBoxLayout()
        self.clipboard_layout.setContentsMargins(-1, -1, 1, -1)
        self.clipboard_layout.setSpacing(0)
        self.command_list = QtWidgets.QListWidget(self.main_left_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding
        )
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
        self.command_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.command_list.setObjectName("command_list")
        item = QtWidgets.QListWidgetItem()
        self.command_list.addItem(item)
        self.clipboard_layout.addWidget(self.command_list)
        self.comand_field = QtWidgets.QTextEdit(self.main_left_layout)
        self.comand_field.setStyleSheet(
            "QTextEdit {\n"
            " background-color: rgb(26, 26, 27);\n"
            " color: rgb(186, 189, 182);\n"
            "    border: 1px solid rgb(50, 50, 50); \n"
            "}\n"
            ""
        )
        self.comand_field.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.comand_field.setObjectName("comand_field")
        self.clipboard_layout.addWidget(self.comand_field)
        self.clipboard_layout.setStretch(0, 1)
        self.clipboard_layout.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.clipboard_layout)
        self.gridLayout_2.addWidget(self.main_left_layout, 0, 0, 1, 1)

        self.all_tabs.addTab(self.main_tab, '')
        self.all_tabs.addTab(PlusTab(), '')

        self.settigs_tab = QtWidgets.QWidget()
        self.settigs_tab.setObjectName("settigs_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.settigs_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.settings_layout = QtWidgets.QVBoxLayout()
        self.settings_layout.setObjectName("settings_layout")
        self.logger_label = QtWidgets.QLabel(self.settigs_tab)
        self.logger_label.setMinimumSize(QtCore.QSize(100, 20))
        self.logger_label.setMaximumSize(QtCore.QSize(100, 20))
        self.logger_label.setStyleSheet("QLabel {color: rgb(186, 189, 182);}")
        self.logger_label.setObjectName("logger_label")
        self.settings_layout.addWidget(self.logger_label)
        self.logger_frame = QtWidgets.QFrame(self.settigs_tab)
        self.logger_frame.setStyleSheet(
            "QFrame{background-color: rgb(35, 35, 35);   border-radius: 5;   border: 1px solid rgb(50, 50, 50); }\n"
            ""
        )
        self.logger_frame.setObjectName("logger_frame")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.logger_frame)
        self.gridLayout_11.setContentsMargins(30, 20, 100, 20)
        self.gridLayout_11.setSpacing(15)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.logger_cb_label = QtWidgets.QLabel(self.logger_frame)
        self.logger_cb_label.setStyleSheet(
            "QLabel {color: rgb(186, 189, 182);border: 0px;}"
        )
        self.logger_cb_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.logger_cb_label.setObjectName("logger_cb_label")
        self.gridLayout_11.addWidget(self.logger_cb_label, 0, 0, 1, 1)
        self.logger_path_label = QtWidgets.QLabel(self.logger_frame)
        self.logger_path_label.setStyleSheet(
            "QLabel {color: rgb(186, 189, 182);border: 0px;}"
        )
        self.logger_path_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.logger_path_label.setObjectName("logger_path_label")
        self.gridLayout_11.addWidget(self.logger_path_label, 2, 0, 1, 1)
        self.logger_spin = QtWidgets.QSpinBox(self.logger_frame)
        self.logger_spin.setStyleSheet(
            "QSpinBox {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "background-color: rgb(35, 35, 35);\n"
            "   padding: 5px;\n"
            "   border-radius: 5;\n"
            "}\n"
            ""
        )
        self.logger_spin.setObjectName("logger_spin")
        self.gridLayout_11.addWidget(self.logger_spin, 1, 1, 1, 1)
        self.logger_quantity_label = QtWidgets.QLabel(self.logger_frame)
        self.logger_quantity_label.setStyleSheet(
            "QLabel {color: rgb(186, 189, 182);border: 0px;}"
        )
        self.logger_quantity_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.logger_quantity_label.setObjectName("logger_quantity_label")
        self.gridLayout_11.addWidget(self.logger_quantity_label, 1, 0, 1, 1)
        self.logger_checkbox = QtWidgets.QCheckBox(self.logger_frame)
        self.logger_checkbox.setStyleSheet(
            "QCheckBox {color: rgb(186, 189, 182);background-color: rgb(35, 35, 35);}"
        )
        self.logger_checkbox.setText("")
        self.logger_checkbox.setObjectName("logger_checkbox")
        self.gridLayout_11.addWidget(self.logger_checkbox, 0, 1, 1, 1)
        self.logger_path_layout = QtWidgets.QHBoxLayout()
        self.logger_path_layout.setSpacing(0)
        self.logger_path_layout.setObjectName("logger_path_layout")
        self.logger_path_field = QtWidgets.QLineEdit(self.logger_frame)
        self.logger_path_field.setStyleSheet(
            "QLineEdit {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-right:0px; \n"
            "background-color: rgb(35, 35, 35);\n"
            "   padding: 5px;\n"
            "   border-top-left-radius: 5;\n"
            "   border-bottom-left-radius: 5;\n"
            "}\n"
            ""
        )
        self.logger_path_field.setObjectName("logger_path_field")
        self.logger_path_layout.addWidget(self.logger_path_field)
        self.logger_folder_button = QtWidgets.QPushButton(self.logger_frame)
        self.logger_folder_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-left: 0px;\n"
            "   border-top-right-radius: 5;\n"
            "   border-bottom-right-radius: 5;\n"
            "   padding: 6px;\n"
            "}\n"
            ""
        )
        self.logger_folder_button.setObjectName("logger_folder_button")
        self.logger_path_layout.addWidget(self.logger_folder_button)
        self.gridLayout_11.addLayout(self.logger_path_layout, 2, 1, 1, 1)
        self.settings_layout.addWidget(self.logger_frame)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.settings_layout.addItem(spacerItem3)
        self.settings_inner_layout = QtWidgets.QGridLayout()
        self.settings_inner_layout.setObjectName("settings_inner_layout")
        self.settings_layout.addLayout(self.settings_inner_layout)
        self.gridLayout_10.addLayout(self.settings_layout, 0, 0, 1, 1)
        self.all_tabs.addTab(self.settigs_tab, "")
        self.all_tabs.addTab(InfoTab(), '')
        self.tab_layout.addWidget(self.all_tabs, 0, 0, 1, 1)
        self.main_w.addLayout(self.tab_layout, 1, 0, 1, 1)
        self.header_frame = QtWidgets.QFrame(self.main_window)
        self.header_frame.setStyleSheet(
            "QFrame {\n" "   background-color: rgb(35, 35, 35);\n" "}"
        )
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_button = QtWidgets.QPushButton(self.header_frame)
        self.edit_button.setMinimumSize(QtCore.QSize(30, 30))
        self.edit_button.setMaximumSize(QtCore.QSize(30, 30))
        self.edit_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border-radius: 5;\n"
            "   padding-left: 5;\n"
            "   padding-right: 5;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(45, 45, 45);\n"
            "}"
        )
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout.addWidget(self.edit_button)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem6)
        self.header_layout = QtWidgets.QGridLayout()
        self.header_layout.setObjectName("header_layout")
        self.profile_icon_button = QtWidgets.QPushButton(self.header_frame)
        self.profile_icon_button.setMinimumSize(QtCore.QSize(30, 30))
        self.profile_icon_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(False)
        font.setWeight(50)
        self.profile_icon_button.setFont(font)
        self.profile_icon_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border-top-left-radius: 5;\n"
            "   border-bottom-left-radius: 5;\n"
            "   padding-left: 5;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(45, 45, 45);\n"
            "}"
        )
        self.profile_icon_button.setObjectName("profile_icon_button")
        self.header_layout.addWidget(self.profile_icon_button, 0, 0, 1, 1)
        self.profile_button = QtWidgets.QPushButton(self.header_frame)
        self.profile_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(False)
        font.setWeight(50)
        self.profile_button.setFont(font)
        self.profile_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border: none;\n"
            "   padding-left: 10;\n"
            "   padding-right: 10;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(45, 45, 45);\n"
            "}"
        )
        self.profile_button.setObjectName("profile_button")
        self.header_layout.addWidget(self.profile_button, 0, 1, 1, 1)
        self.profile_picker_button = QtWidgets.QPushButton(self.header_frame)
        self.profile_picker_button.setMinimumSize(QtCore.QSize(30, 30))
        self.profile_picker_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(False)
        font.setWeight(50)
        self.profile_picker_button.setFont(font)
        self.profile_picker_button.setStyleSheet(
            "QPushButton {\n"
            "   color: rgb(186, 189, 182);\n"
            "   background-color: rgb(35, 35, 35);\n"
            "   border-top-right-radius: 5;\n"
            "   border-bottom-right-radius: 5;\n"
            "   padding-right: 5;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(45, 45, 45);\n"
            "}"
        )
        self.profile_picker_button.setObjectName("profile_picker_button")
        self.header_layout.addWidget(self.profile_picker_button, 0, 2, 1, 1)
        self.connect_button = QtWidgets.QPushButton(self.header_frame)
        self.connect_button.setMinimumSize(QtCore.QSize(30, 30))
        self.connect_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(False)
        font.setWeight(50)
        self.connect_button.setFont(font)
        self.connect_button.setStyleSheet(styles.MAIN_BUTTON)
        self.header_layout.addWidget(self.connect_button, 0, 3, 1, 1)
        self.horizontalLayout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)
        self.sidebar_frame = QtWidgets.QFrame(self.main_window)
        self.sidebar_frame.setStyleSheet(
            "QFrame {\n" "    background-color: rgb(30, 30, 30);\n" "}\n" ""
        )
        self.sidebar_frame.setObjectName("sidebar_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exitor_layout = QtWidgets.QHBoxLayout()
        self.exitor_layout.setSpacing(0)
        self.exitor_layout.setObjectName("exitor_layout")
        self.exit_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.exit_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.exit_button.setObjectName("exit_button")
        self.exitor_layout.addWidget(self.exit_button)
        self.collapse_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.collapse_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.collapse_button.setObjectName("collapse_button")
        self.exitor_layout.addWidget(self.collapse_button)
        self.expand_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.expand_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.expand_button.setObjectName("expand_button")
        self.exitor_layout.addWidget(self.expand_button)
        self.verticalLayout.addLayout(self.exitor_layout)
        self.sidebar_lauout = QtWidgets.QVBoxLayout()
        self.sidebar_lauout.setContentsMargins(15, 10, -1, 30)
        self.sidebar_lauout.setSpacing(10)
        self.sidebar_lauout.setObjectName("sidebar_lauout")
        self.logo_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.logo_button.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_button.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.logo_button.setObjectName("logo_button")
        self.sidebar_lauout.addWidget(self.logo_button)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.sidebar_lauout.addItem(spacerItem7)
        self.main_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.main_button.setMinimumSize(QtCore.QSize(50, 50))
        self.main_button.setMaximumSize(QtCore.QSize(50, 50))
        self.main_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.main_button.setObjectName("main_button")
        self.sidebar_lauout.addWidget(self.main_button)
        self.plus_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.plus_button.setMinimumSize(QtCore.QSize(50, 50))
        self.plus_button.setMaximumSize(QtCore.QSize(50, 50))
        self.plus_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plus_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.plus_button.setObjectName("plus_button")
        self.sidebar_lauout.addWidget(self.plus_button)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.sidebar_lauout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.sidebar_lauout.addItem(spacerItem9)
        self.settings_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.settings_button.setMinimumSize(QtCore.QSize(50, 50))
        self.settings_button.setMaximumSize(QtCore.QSize(50, 50))
        self.settings_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.settings_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.settings_button.setObjectName("settings_button")
        self.sidebar_lauout.addWidget(self.settings_button)
        self.info_button = QtWidgets.QPushButton(self.sidebar_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy)
        self.info_button.setMinimumSize(QtCore.QSize(50, 50))
        self.info_button.setMaximumSize(QtCore.QSize(50, 50))
        self.info_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border-top-left-radius: 5;\n"
            "    border-bottom-left-radius: 5;\n"
            "    border-top-right-radius: 5;\n"
            "    border-bottom-right-radius: 5;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(40, 40, 40);\n"
            "}"
        )
        self.info_button.setObjectName("info_button")
        self.sidebar_lauout.addWidget(self.info_button)
        self.verticalLayout.addLayout(self.sidebar_lauout)
        self.main_layout.addWidget(self.sidebar_frame, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.main_layout)
        MainWindow.setCentralWidget(self.main_window)

        self.retranslateUi(MainWindow)
        self.all_tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clear_button.setText(_translate("MainWindow", "clear"))
        __sortingEnabled = self.receiver_list.isSortingEnabled()
        self.receiver_list.setSortingEnabled(False)
        item = self.receiver_list.item(0)
        item.setText(_translate("MainWindow", "New Message"))
        item = self.receiver_list.item(1)
        item.setText(_translate("MainWindow", "New Message"))
        self.receiver_list.setSortingEnabled(__sortingEnabled)
        self.convertor_button.setText(_translate("MainWindow", "MsgPack"))
        self.convertor_picker_button.setText(_translate("MainWindow", "∇"))
        self.all_button.setText(_translate("MainWindow", "All"))
        self.received_button.setText(_translate("MainWindow", "Received"))
        self.published_button.setText(_translate("MainWindow", "Published"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.add_clipboard_button.setText(_translate("MainWindow", "Add to Clipboard"))
        self.qos_button.setText(_translate("MainWindow", "QoS 0"))
        self.qos_picker_button.setText(_translate("MainWindow", "∇"))
        self.publish_button.setText(_translate("MainWindow", "Publish"))
        __sortingEnabled = self.command_list.isSortingEnabled()
        self.command_list.setSortingEnabled(False)
        item = self.command_list.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        self.command_list.setSortingEnabled(__sortingEnabled)
        self.all_tabs.setTabText(
            self.all_tabs.indexOf(self.main_tab), _translate("MainWindow", "Page")
        )
        self.logger_label.setText(_translate("MainWindow", "Logger"))
        self.logger_cb_label.setText(_translate("MainWindow", "Logger"))
        self.logger_path_label.setText(_translate("MainWindow", "Logger Path"))
        self.logger_quantity_label.setText(_translate("MainWindow", "Logger Quantity"))
        self.logger_folder_button.setText(_translate("MainWindow", "fff"))
        self.all_tabs.setTabText(
            self.all_tabs.indexOf(self.settigs_tab), _translate("MainWindow", "Page")
        )
        self.edit_button.setText(_translate("MainWindow", "edit"))
        self.profile_icon_button.setText(_translate("MainWindow", "🄰"))
        self.profile_button.setText(_translate("MainWindow", "Profile Name"))
        self.profile_picker_button.setText(_translate("MainWindow", "∇"))
        self.connect_button.setText(_translate("MainWindow", "▶"))
        self.exit_button.setText(_translate("MainWindow", "x"))
        self.collapse_button.setText(_translate("MainWindow", "_"))
        self.expand_button.setText(_translate("MainWindow", "e"))
        self.logo_button.setText(_translate("MainWindow", "logo"))
        self.main_button.setText(_translate("MainWindow", "main"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.settings_button.setText(_translate("MainWindow", "stg"))
        self.info_button.setText(_translate("MainWindow", "inf"))
