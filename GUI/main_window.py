from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from connections.plus_tab import EditTab, PlusTab
from GUI import styles
from GUI.interface_utils import create_button, create_label
from GUI.tabs.info_tab import InfoTab
from GUI.tabs.main_tab import MainTabUI, vertical_spacer


class MqttHubUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 50, 1066, 904)
        self.drag_pos = None

        self.sidebar_layout = QtWidgets.QVBoxLayout()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None

    def setup_ui(self):
        self.main_window = QtWidgets.QWidget(self)
        self.main_window.setStyleSheet(
            "QWidget {\n" "    background-color: rgb(30, 30, 30);\n" "}\n" ""
        )
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_window)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_w = QtWidgets.QGridLayout()
        self.main_w.setSpacing(0)

        self.tab_layout = QtWidgets.QGridLayout()
        self.tab_layout.setSpacing(0)
        self.all_tabs = QtWidgets.QTabWidget(self.main_window)
        self.all_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.all_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.all_tabs.setElideMode(QtCore.Qt.ElideRight)
        self.all_tabs.setUsesScrollButtons(False)
        self.all_tabs.setTabsClosable(False)
        self.all_tabs.setMovable(False)
        self.all_tabs.setTabBarAutoHide(False)
        self.all_tabs.addTab(MainTabUI(), '')
        self.all_tabs.addTab(PlusTab(), '')
        self.edit_tab = EditTab()
        self.all_tabs.addTab(self.edit_tab, '')

        self.settigs_tab = QtWidgets.QWidget()
        self.gridLayout_10 = QtWidgets.QGridLayout(self.settigs_tab)
        self.settings_layout = QtWidgets.QVBoxLayout()
        self.logger_label = QtWidgets.QLabel(self.settigs_tab)
        self.logger_label.setMinimumSize(QtCore.QSize(100, 20))
        self.logger_label.setMaximumSize(QtCore.QSize(100, 20))
        self.logger_label.setStyleSheet("QLabel {color: rgb(186, 189, 182);}")
        self.settings_layout.addWidget(self.logger_label)
        self.logger_frame = QtWidgets.QFrame(self.settigs_tab)
        self.logger_frame.setStyleSheet(
            "QFrame{background-color: rgb(35, 35, 35); border-radius: 5; border: 1px solid rgb(50, 50, 50); }"
        )
        self.gridLayout_11 = QtWidgets.QGridLayout(self.logger_frame)
        self.gridLayout_11.setContentsMargins(30, 20, 100, 20)
        self.gridLayout_11.setSpacing(15)
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
        self.gridLayout_11.addWidget(self.logger_spin, 1, 1, 1, 1)
        self.logger_quantity_label = QtWidgets.QLabel(self.logger_frame)
        self.logger_quantity_label.setStyleSheet(
            "QLabel {color: rgb(186, 189, 182);border: 0px;}"
        )
        self.logger_quantity_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.gridLayout_11.addWidget(self.logger_quantity_label, 1, 0, 1, 1)
        self.logger_checkbox = QtWidgets.QCheckBox(self.logger_frame)
        self.logger_checkbox.setStyleSheet(
            "QCheckBox {color: rgb(186, 189, 182);background-color: rgb(35, 35, 35);}"
        )
        self.logger_checkbox.setText("")
        self.gridLayout_11.addWidget(self.logger_checkbox, 0, 1, 1, 1)
        self.logger_path_layout = QtWidgets.QHBoxLayout()
        self.logger_path_layout.setSpacing(0)
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
        self.logger_path_layout.addWidget(self.logger_folder_button)
        self.gridLayout_11.addLayout(self.logger_path_layout, 2, 1, 1, 1)
        self.settings_layout.addWidget(self.logger_frame)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.settings_layout.addItem(spacerItem3)
        self.settings_inner_layout = QtWidgets.QGridLayout()
        self.settings_layout.addLayout(self.settings_inner_layout)
        self.gridLayout_10.addLayout(self.settings_layout, 0, 0, 1, 1)
        self.all_tabs.addTab(self.settigs_tab, "")
        self.all_tabs.addTab(InfoTab(), '')
        self.tab_layout.addWidget(self.all_tabs, 0, 0, 1, 1)
        self.main_w.addLayout(self.tab_layout, 1, 0, 1, 1)
        self.all_tabs.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.all_tabs.tabBar().hide()
        self.all_tabs.setCurrentIndex(0)

        self.sidebar_frame = QtWidgets.QFrame(self.main_window)
        self.sidebar_frame.setStyleSheet('QFrame {background-color: rgb(30, 30, 30);}')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_frame)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.exitor_layout = QtWidgets.QHBoxLayout()
        self.exitor_layout.setSpacing(10)

        self.exit_button = create_button(
            '',
            self.sidebar_frame,
            styles.EXIT_BUTTON,
            min_size=12,
            max_size=12,
            add_layout=self.exitor_layout,
        )
        self.exit_button.clicked.connect(self.close)

        self.collapse_button = create_button(
            '',
            self.sidebar_frame,
            styles.EXIT_BUTTON,
            min_size=12,
            max_size=12,
            add_layout=self.exitor_layout,
        )
        self.expand_button = create_button(
            '',
            self.sidebar_frame,
            styles.EXIT_BUTTON,
            min_size=12,
            max_size=12,
            add_layout=self.exitor_layout,
        )

        self.verticalLayout.addLayout(self.exitor_layout)
        self.sidebar_layout.setContentsMargins(20, 30, 20, 30)
        self.sidebar_layout.setSpacing(20)
        self.logo_button = create_button(
            '',
            self.sidebar_frame,
            min_size=50,
            max_size=50,
            add_layout=self.sidebar_layout,
        )
        self.logo_button.setStyleSheet(styles.sidebar_button('GUI/icons/logo-icon.png'))

        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.sidebar_layout.addItem(spacerItem7)
        self.main_button = create_button(
            '',
            self.sidebar_frame,
            min_size=50,
            max_size=50,
            add_layout=self.sidebar_layout,
        )
        self.main_button.setStyleSheet(styles.sidebar_button('GUI/icons/main-icon.png'))

        self.plus_button = create_button(
            '',
            self.sidebar_frame,
            min_size=50,
            max_size=50,
            add_layout=self.sidebar_layout,
        )
        self.plus_button.setStyleSheet(styles.sidebar_button('GUI/icons/plus-icon.png'))

        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.sidebar_layout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.sidebar_layout.addItem(spacerItem9)

        self.settings_button = create_button(
            '',
            self.sidebar_frame,
            min_size=(50, 50),
            max_size=(50, 50),
            add_layout=self.sidebar_layout,
        )
        self.settings_button.setStyleSheet(
            styles.sidebar_button('GUI/icons/settings-icon.png')
        )

        self.info_button = create_button(
            '',
            self.sidebar_frame,
            min_size=(50, 50),
            max_size=(50, 50),
            add_layout=self.sidebar_layout,
        )
        self.info_button.setStyleSheet(styles.sidebar_button('GUI/icons/info-icon.png'))

        self.verticalLayout.addLayout(self.sidebar_layout)
        self.main_layout.addWidget(self.sidebar_frame, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.main_layout)
        self.setCentralWidget(self.main_window)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.all_tabs.setCurrentIndex(0)

        self.header_layout = QtWidgets.QGridLayout()
        self.setup_plus_header()
        self.setup_main_header()
        self.main_button.clicked.connect(self.open_main_tab)
        self.plus_button.clicked.connect(self.open_plus_tab)

    def setup_main_header(self):
        self.header_frame = QtWidgets.QFrame(self.main_window)
        self.header_frame.setStyleSheet(
            "QFrame {\n" "   background-color: rgb(35, 35, 35);\n" "}"
        )
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout.setSpacing(15)
        self.edit_button = create_button(
            '',
            self.header_frame,
            min_size=30,
            max_size=30,
            add_layout=self.horizontalLayout,
        )
        self.edit_button.setStyleSheet(styles.header_button('GUI/icons/edit-icon.png'))

        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem6)
        self.header_layout = QtWidgets.QGridLayout()

        self.profile_button = create_button(
            'No Profile',
            self.header_frame,
            min_size=(0, 30),
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )
        self.profile_button.setStyleSheet(
            'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border: none;'
            'border-radius: 5px; padding: 0px 10px, 5px,} QPushButton:hover {background-color: rgb(45, 45, 45);}'
        )
        self.profile_button.setIcon(QIcon('GUI/icons/expand-profile-icon.png'))
        self.profile_button.setIconSize(QSize(24, 24))
        self.profile_button.setLayoutDirection(Qt.RightToLeft)

        self.connect_button = create_button(
            '',
            self.header_frame,
            min_size=30,
            max_size=30,
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
        )
        self.connect_button.setStyleSheet(
            styles.header_button('GUI/icons/connect-icon.png')
        )

        self.horizontalLayout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)
        self.edit_button.clicked.connect(
            self.open_edit_tab
        )  # TODO: replace to connections

    def setup_plus_header(self):
        self.header_layout.addItem(vertical_spacer, 0, 0, 1, 1)
        self.header_frame = QtWidgets.QFrame(self.main_window)
        self.header_frame.setStyleSheet(
            "QFrame {\n" "   background-color: rgb(35, 35, 35);\n" "}"
        )

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setContentsMargins(10, 5, 25, 5)
        self.horizontalLayout.setSpacing(20)

        self.horizontalLayout.addItem(vertical_spacer)

        self.profile_name = create_label(
            'New Profile',
            self.header_frame,
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )

        self.header_layout.addItem(vertical_spacer, 0, 2, 1, 1)

        self.save_button = create_button(
            'Save',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
        )
        self.connect_button = create_button(
            'Connect',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 4, 1, 1],
        )

        self.horizontalLayout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)

    def setup_edit_header(self):
        self.header_layout.addItem(vertical_spacer, 0, 0, 1, 1)
        self.header_frame = QtWidgets.QFrame(self.main_window)
        self.header_frame.setStyleSheet(
            "QFrame {\n" "   background-color: rgb(35, 35, 35);\n" "}"
        )

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setContentsMargins(10, 5, 25, 5)
        self.horizontalLayout.setSpacing(20)

        self.horizontalLayout.addItem(vertical_spacer)
        self.header_layout = QtWidgets.QGridLayout()

        self.profile_name = create_label(
            'New Profile',
            self.header_frame,
            add_layout=self.header_layout,
            add_params=[0, 1, 1, 1],
        )

        self.header_layout.addItem(vertical_spacer, 0, 2, 1, 1)

        self.save_button = create_button(
            'Save',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 3, 1, 1],
        )
        self.connect_button = create_button(
            'Connect',
            self.header_frame,
            styles.MAIN_BUTTON,
            add_layout=self.header_layout,
            add_params=[0, 4, 1, 1],
        )

        self.horizontalLayout.addLayout(self.header_layout)
        self.main_w.addWidget(self.header_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.main_w, 0, 1, 1, 1)

    def open_main_tab(self):
        self.all_tabs.setCurrentIndex(0)
        self.setup_main_header()

    def open_plus_tab(self):
        self.all_tabs.setCurrentIndex(1)
        self.setup_plus_header()

    def open_edit_tab(self):
        self.all_tabs.setCurrentIndex(2)
        self.setup_edit_header()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.logger_label.setText(_translate("MainWindow", "Logger"))
        self.logger_cb_label.setText(_translate("MainWindow", "Logger"))
        self.logger_path_label.setText(_translate("MainWindow", "Logger Path"))
        self.logger_quantity_label.setText(_translate("MainWindow", "Logger Quantity"))
        self.logger_folder_button.setText(_translate("MainWindow", "fff"))
