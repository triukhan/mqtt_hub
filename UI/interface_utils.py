from enum import Enum

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import (
    QCheckBox,
    QFrame,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
)

from UI import styles

LABEL_ALIGNMENT = (
    QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
)


class Spacer(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


def create_label(  # TODO: typing
    text: str,
    main_layout,
    add_layout=None,
    add_params: list | None = None,
    style: str = styles.LABEL,
    *,
    min_size: list | None = None,
    max_size: list | None = None,
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

    if min_size is not None:
        label.setMinimumSize(QtCore.QSize(*min_size))
    if max_size is not None:
        label.setMaximumSize(QtCore.QSize(*max_size))

    return label


def create_field(main_layout, add_layout=None, add_params: list | None = None):
    field = QLineEdit(main_layout)
    field.setStyleSheet(styles.FIELD)

    if add_layout is not None:
        if add_params is not None:
            add_layout.addWidget(field, *add_params)
        else:
            add_layout.addWidget(field)

    return field


def create_checkbox(
    main_layout, add_layout=None, add_params: list | None = None, text: str = ''
):
    checkbox = QCheckBox(main_layout)
    checkbox.setStyleSheet(styles.CHECK_BOX)
    checkbox.setText(text)
    if add_params:
        add_layout.addWidget(checkbox, *add_params)
    else:
        add_layout.addWidget(checkbox)
    return checkbox


def create_radio(text: str, main_layout, add_layout, add_params: list | None = None):
    radio = QRadioButton(main_layout)
    radio.setText(text)
    radio.setStyleSheet(styles.RADIO)
    add_layout.addWidget(radio)


def create_frame(main_layout, style: str | bool = styles.FRAME_PART, add_layout=None):
    frame = QFrame(main_layout)
    if style:
        frame.setStyleSheet(style)

    if add_layout is not None:
        add_layout.addWidget(frame)

    return frame


def create_layout(
    layout_type, margins: list | int | None = None, spacing: int = 0, out_layout=None
):
    if out_layout is not None:
        layout = layout_type(out_layout)
    else:
        layout = layout_type()

    if isinstance(margins, int):
        margins = [margins for _ in range(4)]

    if margins is not None:
        layout.setContentsMargins(*margins)
    layout.setSpacing(spacing)
    return layout


def create_button(
    text,
    layout,
    min_size=None,
    max_size=None,
    add_layout=None,
    add_params=None,
    style=styles.APP_BUTTON,
    font=None,
):  # TODO: font
    button = QPushButton(layout)
    button.setText(text)
    button.setStyleSheet(style)
    if min_size:
        if isinstance(min_size, int):
            button.setMinimumSize(QtCore.QSize(min_size, min_size))
        else:
            button.setMinimumSize(QtCore.QSize(*min_size))
    if max_size:
        if isinstance(max_size, int):
            button.setMaximumSize(QtCore.QSize(max_size, max_size))
        else:
            button.setMaximumSize(QtCore.QSize(*max_size))

    if add_layout is not None:
        if add_params is not None:
            add_layout.addWidget(button, *add_params)
        else:
            add_layout.addWidget(button)

    return button


def create_list(layout, style=styles.LIST, add_layout=None):
    qlist = QListWidget(layout)
    qlist.setStyleSheet(style)
    qlist.setFrameShape(QFrame.NoFrame)

    if add_layout is not None:
        add_layout.addWidget(qlist)

    return qlist


def create_spacer(spacer_type: Spacer):
    size = (
        (QSizePolicy.Expanding, QSizePolicy.Minimum)
        if spacer_type == Spacer.HORIZONTAL
        else (QSizePolicy.Minimum, QSizePolicy.Expanding)
    )
    return QSpacerItem(40, 20, *size)


def set_button_text(button, text, max_width):
    font_metrics = QFontMetrics(button.font())
    elided_text = font_metrics.elidedText(text, Qt.ElideRight, max_width)
    button.setText(elided_text)


def set_topic_color(topic, tag):
    if topic.color:
        if color := topic.color:
            tag.setStyleSheet(
                tag.styleSheet()
                + f'QFrame {{border-left: 2px solid {color};}} QFrame:hover {{border-left: 2px solid {color};}}'
            )


def select_tag(tag):
    border = '2px solid rgb(70, 70, 70);'
    style = (
        f'QFrame {{border-right: {border} border-top: {border} border-bottom: {border}}}'
        if 'border-left' in tag.styleSheet()
        else f'QFrame {{border: {border}}}'
    )
    tag.setStyleSheet(tag.styleSheet() + style)


def deselect_tag(tag):
    style = (
        'QFrame {border-right: none; border-top: none; border-bottom: none;}'
        if 'border-left' in tag.styleSheet()
        else 'QFrame {border: none;}'
    )
    tag.setStyleSheet(tag.styleSheet() + style)
