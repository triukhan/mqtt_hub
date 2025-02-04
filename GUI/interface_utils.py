from PyQt5 import QtCore
from PyQt5.QtWidgets import QCheckBox, QFrame, QLabel, QLineEdit, QRadioButton

from GUI import styles

LABEL_ALIGNMENT = (
    QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
)


def create_label(  # TODO: typing
    text: str,
    main_layout,
    add_layout=None,
    add_params: list | None = None,
    style: str = styles.LABEL,
    *,
    max_size: tuple | None = None,
    min_size: tuple | None = None,
):
    label = QLabel(main_layout)
    label.setText(text)
    label.setStyleSheet(style)
    label.setAlignment(LABEL_ALIGNMENT)

    if add_layout is not None:
        if add_params is not None:
            add_layout.addWidget(label, *add_params)
        else:
            add_layout.addWidget(label)

    if max_size is not None:
        label.setMinimumSize(QtCore.QSize(*max_size))
    if min_size is not None:
        label.setMaximumSize(QtCore.QSize(*min_size))

    return label


def create_field(main_layout, add_layout=None, add_params: list | None = None):
    field = QLineEdit(main_layout)
    field.setStyleSheet(styles.FIELD)

    if add_layout is not None:
        add_layout.addWidget(field, *add_params)

    return field


def create_checkbox(
    main_layout, add_layout=None, add_params: list | None = None, text: str = ''
):
    checkbox = QCheckBox(main_layout)
    checkbox.setStyleSheet(styles.CHECK_BOX)
    checkbox.setText(text)
    add_layout.addWidget(checkbox, *add_params)
    return checkbox


def create_radio(text: str, main_layout, add_layout, add_params: list | None = None):
    radio = QRadioButton(main_layout)
    radio.setText(text)
    radio.setStyleSheet(styles.RADIO)
    add_layout.addWidget(radio)


def create_frame(main_layout, style: str = styles.FRAME_PART, add_layout=None):
    frame = QFrame(main_layout)
    frame.setStyleSheet(style)

    if add_layout is not None:
        add_layout.addWidget(frame)

    return frame
