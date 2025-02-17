from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTextEdit


class ClipboardDialogUI(object):
    def setup_ui(self, edit_subscr_dialog):
        edit_subscr_dialog.resize(365, 190)
        edit_subscr_dialog.setStyleSheet(
            "QWidget {\n"
            "    background-color: rgb(35, 35, 35);\n"
            "    color: rgb(186, 189, 182)\n"
            "}"
        )
        self.gridLayout = QtWidgets.QGridLayout(edit_subscr_dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.edit_subscr_frame = QtWidgets.QFrame(edit_subscr_dialog)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.edit_subscr_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.heade_edit_subscr_frame = QtWidgets.QFrame(self.edit_subscr_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.heade_edit_subscr_frame.sizePolicy().hasHeightForWidth()
        )
        self.heade_edit_subscr_frame.setSizePolicy(sizePolicy)
        self.heade_edit_subscr_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.heade_edit_subscr_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.heade_edit_subscr_frame.setStyleSheet(
            "QFrame {border-bottom: 1px solid rgb(50, 50, 50)}"
        )
        self.heade_edit_subscr_frame.setObjectName("heade_edit_subscr_frame")
        self.header_edit_subscr_layout = QtWidgets.QHBoxLayout(
            self.heade_edit_subscr_frame
        )
        self.header_edit_subscr_layout.setContentsMargins(15, 0, 15, 0)
        self.header_edit_subscr_layout.setSpacing(15)
        self.header_edit_subscr_layout.setObjectName("header_edit_subscr_layout")
        self.edit_subscr_label = QtWidgets.QLabel(self.heade_edit_subscr_frame)
        self.edit_subscr_label.setMinimumSize(QtCore.QSize(30, 30))
        self.edit_subscr_label.setMaximumSize(QtCore.QSize(200, 30))
        self.edit_subscr_label.setStyleSheet("QLabel {border: none}")
        self.header_edit_subscr_layout.addWidget(self.edit_subscr_label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.header_edit_subscr_layout.addItem(spacerItem)
        self.exit_label = QtWidgets.QPushButton(self.heade_edit_subscr_frame)
        self.exit_label.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_label.setMaximumSize(QtCore.QSize(30, 30))
        self.exit_label.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(35, 35, 35);\n"
            "    padding: 10px; border: none;\n"
            "    \n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: rgb(210, 210, 210);\n"
            "}"
        )
        self.header_edit_subscr_layout.addWidget(self.exit_label)
        self.verticalLayout.addWidget(self.heade_edit_subscr_frame)
        self.body_edit_subscr_layout = QtWidgets.QVBoxLayout()
        self.body_edit_subscr_layout.setSpacing(0)
        self.body_edit_subscr_layout.setObjectName("body_edit_subscr_layout")
        self.topic_layout = QtWidgets.QVBoxLayout()
        self.topic_layout.setContentsMargins(20, 10, 20, 10)
        self.topic_layout.setSpacing(10)
        self.name_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.name_label.setMinimumSize(QtCore.QSize(0, 30))
        self.name_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.topic_layout.addWidget(self.name_label)

        self.name_field = QtWidgets.QLineEdit(self.edit_subscr_frame)
        self.name_field.setStyleSheet(
            "QLineEdit {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-radius: 5;\n"
            "   padding: 5px;\n"
            "background-color: rgb(35, 35, 35);\n"
            "}"
        )
        self.topic_layout.addWidget(self.name_field)

        self.body_edit_subscr_layout.addLayout(self.topic_layout)

        self.text_layout = QtWidgets.QVBoxLayout()
        self.text_layout.setContentsMargins(20, 10, 20, 10)
        self.text_layout.setSpacing(10)
        self.text_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.text_label.setMinimumSize(QtCore.QSize(0, 30))
        self.text_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.text_label.setText('Text')
        self.text_layout.addWidget(self.text_label)

        self.text_field = QTextEdit(self.edit_subscr_frame)
        self.text_layout.addWidget(self.text_field)

        self.body_edit_subscr_layout.addLayout(self.text_layout)

        self.save_layout = QtWidgets.QHBoxLayout()
        self.save_layout.setContentsMargins(-1, 15, 20, 15)
        self.save_layout.setSpacing(15)
        self.save_layout.setObjectName("save_layout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.save_layout.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(self.edit_subscr_frame)
        self.cancel_button.setStyleSheet(
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
        self.save_layout.addWidget(self.cancel_button)
        self.save_button = QtWidgets.QPushButton(self.edit_subscr_frame)
        self.save_button.setStyleSheet(
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
        self.save_layout.addWidget(self.save_button)
        self.body_edit_subscr_layout.addLayout(self.save_layout)
        self.verticalLayout.addLayout(self.body_edit_subscr_layout)
        self.gridLayout.addWidget(self.edit_subscr_frame, 0, 0, 1, 1)

        self.retranslateUi(edit_subscr_dialog)
        QtCore.QMetaObject.connectSlotsByName(edit_subscr_dialog)

    def retranslateUi(self, edit_subscr_dialog):
        _translate = QtCore.QCoreApplication.translate
        edit_subscr_dialog.setWindowTitle(_translate("edit_subscr_dialog", "Dialog"))
        self.edit_subscr_label.setText(
            _translate("edit_subscr_dialog", "Add to Clipboard")
        )
        self.exit_label.setText(_translate("edit_subscr_dialog", "x"))
        self.name_label.setText(
            _translate("edit_subscr_dialog", "Enter a name for the Clipboard Message")
        )
        self.cancel_button.setText(_translate("edit_subscr_dialog", "Cancel"))
        self.save_button.setText(_translate("edit_subscr_dialog", "Save"))
