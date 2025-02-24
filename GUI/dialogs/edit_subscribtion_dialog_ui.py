from PyQt5 import QtCore, QtWidgets


class EditSubscribeDialogUI(object):
    def setup_ui(self, edit_subscr_dialog):
        edit_subscr_dialog.resize(522, 530)
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
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.edit_subscr_label.setObjectName("edit_subscr_label")
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
        self.exit_label.setObjectName("exit_label")
        self.header_edit_subscr_layout.addWidget(self.exit_label)
        self.verticalLayout.addWidget(self.heade_edit_subscr_frame)
        self.body_edit_subscr_layout = QtWidgets.QVBoxLayout()
        self.body_edit_subscr_layout.setSpacing(0)
        self.body_edit_subscr_layout.setObjectName("body_edit_subscr_layout")
        self.topic_layout = QtWidgets.QVBoxLayout()
        self.topic_layout.setContentsMargins(20, 10, 20, 10)
        self.topic_layout.setSpacing(10)
        self.topic_layout.setObjectName("topic_layout")
        self.topic_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.topic_label.setMinimumSize(QtCore.QSize(0, 30))
        self.topic_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.topic_label.setObjectName("topic_label")
        self.topic_layout.addWidget(self.topic_label)
        self.topic_field = QtWidgets.QLineEdit(self.edit_subscr_frame)
        self.topic_field.setStyleSheet(
            "QLineEdit {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-radius: 5;\n"
            "   padding: 5px;\n"
            "background-color: rgb(35, 35, 35);\n"
            "}"
        )
        self.topic_field.setObjectName("topic_field")
        self.topic_layout.addWidget(self.topic_field)
        self.body_edit_subscr_layout.addLayout(self.topic_layout)
        self.alias_layout = QtWidgets.QVBoxLayout()
        self.alias_layout.setContentsMargins(20, 0, 20, 5)
        self.alias_layout.setSpacing(10)
        self.alias_layout.setObjectName("alias_layout")
        self.alias_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.alias_label.setMinimumSize(QtCore.QSize(0, 35))
        self.alias_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.alias_label.setObjectName("alias_label")
        self.alias_layout.addWidget(self.alias_label)
        self.alias_field = QtWidgets.QLineEdit(self.edit_subscr_frame)
        self.alias_field.setStyleSheet(
            "QLineEdit {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-radius: 5;\n"
            "   padding: 5px;\n"
            "background-color: rgb(35, 35, 35);\n"
            "}"
        )
        self.alias_layout.addWidget(self.alias_field)
        self.body_edit_subscr_layout.addLayout(self.alias_layout)
        self.qos_color_layout = QtWidgets.QGridLayout()
        self.qos_color_layout.setContentsMargins(20, 15, 20, 15)
        self.qos_color_layout.setHorizontalSpacing(20)
        self.qos_color_layout.setVerticalSpacing(15)
        self.qos_color_layout.setObjectName("qos_color_layout")
        self.qos_field = QtWidgets.QLineEdit(self.edit_subscr_frame)
        self.qos_field.setMinimumSize(QtCore.QSize(230, 30))
        self.qos_field.setMaximumSize(QtCore.QSize(200, 30))
        self.qos_field.setStyleSheet(
            "QLineEdit {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-radius: 5;\n"
            "   padding: 5px;\n"
            "background-color: rgb(35, 35, 35);\n"
            "}"
        )
        self.qos_field.setObjectName("qos_field")
        self.qos_color_layout.addWidget(self.qos_field, 1, 0, 1, 1)
        self.qos_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.qos_label.setObjectName("qos_label")
        self.qos_color_layout.addWidget(self.qos_label, 0, 0, 1, 1)
        self.color_layout = QtWidgets.QHBoxLayout()
        self.color_layout.setObjectName("color_layout")
        self.color_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.color_label.setObjectName("color_label")
        self.color_layout.addWidget(self.color_label)
        self.color_button = QtWidgets.QPushButton(self.edit_subscr_frame)
        self.color_button.setMinimumSize(QtCore.QSize(30, 30))
        self.color_button.setMaximumSize(QtCore.QSize(30, 30))
        self.color_button.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(186, 189, 182);\n"
            "    background-color: rgb(35, 35, 35);\n"
            "    padding: 10px;    border: 1px solid rgb(50, 50, 50); \n"
            "    \n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: rgb(210, 210, 210);\n"
            "}"
        )
        self.color_button.setObjectName("color_button")
        self.color_layout.addWidget(self.color_button)
        self.qos_color_layout.addLayout(self.color_layout, 0, 3, 1, 1)
        self.color_field = QtWidgets.QLineEdit(self.edit_subscr_frame)
        self.color_field.setMinimumSize(QtCore.QSize(230, 30))
        self.color_field.setMaximumSize(QtCore.QSize(200, 30))
        self.color_field.setStyleSheet(
            "QLineEdit {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-radius: 5;\n"
            "   padding: 5px;\n"
            "background-color: rgb(35, 35, 35);\n"
            "}"
        )
        self.color_field.setObjectName("color_field")
        self.qos_color_layout.addWidget(self.color_field, 1, 3, 1, 1)
        self.body_edit_subscr_layout.addLayout(self.qos_color_layout)
        self.no_local_layout = QtWidgets.QHBoxLayout()
        self.no_local_layout.setContentsMargins(20, 15, 20, 15)
        self.no_local_layout.setObjectName("no_local_layout")
        self.no_local_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.no_local_label.setObjectName("no_local_label")
        self.no_local_layout.addWidget(self.no_local_label)
        self.no_local_checkbox = QtWidgets.QCheckBox(self.edit_subscr_frame)
        self.no_local_checkbox.setText("")
        self.no_local_checkbox.setObjectName("no_local_checkbox")
        self.no_local_layout.addWidget(self.no_local_checkbox)
        self.body_edit_subscr_layout.addLayout(self.no_local_layout)
        self.retain_published_layout = QtWidgets.QHBoxLayout()
        self.retain_published_layout.setContentsMargins(20, 15, 20, 15)
        self.retain_published_layout.setObjectName("retain_published_layout")
        self.retain_published_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.retain_published_label.setObjectName("retain_published_label")
        self.retain_published_layout.addWidget(self.retain_published_label)
        self.retain_published_checkbox = QtWidgets.QCheckBox(self.edit_subscr_frame)
        self.retain_published_checkbox.setText("")
        self.retain_published_checkbox.setObjectName("retain_published_checkbox")
        self.retain_published_layout.addWidget(self.retain_published_checkbox)
        self.body_edit_subscr_layout.addLayout(self.retain_published_layout)
        self.retain_handlin_layout = QtWidgets.QHBoxLayout()
        self.retain_handlin_layout.setContentsMargins(20, 15, 20, 15)
        self.retain_handlin_layout.setSpacing(15)
        self.retain_handlin_layout.setObjectName("retain_handlin_layout")
        self.retain_handling_label = QtWidgets.QLabel(self.edit_subscr_frame)
        self.retain_handling_label.setObjectName("retain_handling_label")
        self.retain_handlin_layout.addWidget(self.retain_handling_label)
        self.retain_handling_field = QtWidgets.QLineEdit(self.edit_subscr_frame)
        self.retain_handling_field.setStyleSheet(
            "QLineEdit {\n"
            "   color: rgb(186, 189, 182);\n"
            "   border: 1px solid rgb(50, 50, 50); \n"
            "   border-radius: 5;\n"
            "   padding: 5px;\n"
            "background-color: rgb(35, 35, 35);\n"
            "}"
        )
        self.retain_handlin_layout.addWidget(self.retain_handling_field)
        self.body_edit_subscr_layout.addLayout(self.retain_handlin_layout)
        self.save_layout = QtWidgets.QHBoxLayout()
        self.save_layout.setContentsMargins(-1, 15, 20, 15)
        self.save_layout.setSpacing(15)
        self.save_layout.setObjectName("save_layout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.save_layout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.edit_subscr_frame)
        self.pushButton_2.setStyleSheet(
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.save_layout.addWidget(self.pushButton_2)
        self.save_topic_button = QtWidgets.QPushButton(self.edit_subscr_frame)
        self.save_topic_button.setStyleSheet(
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
        self.save_layout.addWidget(self.save_topic_button)
        self.body_edit_subscr_layout.addLayout(self.save_layout)
        self.verticalLayout.addLayout(self.body_edit_subscr_layout)
        self.gridLayout.addWidget(self.edit_subscr_frame, 0, 0, 1, 1)

        self.retranslateUi(edit_subscr_dialog)
        QtCore.QMetaObject.connectSlotsByName(edit_subscr_dialog)

    def retranslateUi(self, edit_subscr_dialog):
        _translate = QtCore.QCoreApplication.translate
        edit_subscr_dialog.setWindowTitle(_translate("edit_subscr_dialog", "Dialog"))
        self.edit_subscr_label.setText(
            _translate("edit_subscr_dialog", "Edit Subscribition")
        )
        self.exit_label.setText(_translate("edit_subscr_dialog", "x"))
        self.topic_label.setText(_translate("edit_subscr_dialog", " Topic"))
        self.alias_label.setText(_translate("edit_subscr_dialog", " Alias"))
        self.qos_label.setText(_translate("edit_subscr_dialog", "Qos"))
        self.color_label.setText(_translate("edit_subscr_dialog", "Color"))
        self.color_button.setText(_translate("edit_subscr_dialog", "color"))
        self.no_local_label.setText(_translate("edit_subscr_dialog", "No Local Flag"))
        self.retain_published_label.setText(
            _translate("edit_subscr_dialog", "Retain as Published Flag")
        )
        self.retain_handling_label.setText(
            _translate("edit_subscr_dialog", "Retain Handling")
        )
        self.pushButton_2.setText(_translate("edit_subscr_dialog", "Cancel"))
        self.save_topic_button.setText(_translate("edit_subscr_dialog", "Save"))
