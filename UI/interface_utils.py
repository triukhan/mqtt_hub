from enum import Enum

from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtGui import QFont, QFontMetrics, QIcon, QPen, QColor
from PyQt5.QtWidgets import (
    QCheckBox,
    QFrame,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenu,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem, QStyledItemDelegate,
)

from settings.topic import Topic
from UI import styles
from UI.icons.icons import EXPAND_ICON
from UI.styles import MENU, EXPAND_BUTTON

LABEL_RIGHT_ALIGNMENT = (
    QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
)
LABEL_LEFT_ALIGNMENT = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter


class Spacer(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


def create_label(
    text: str,
    main_layout,
    add_layout=None,
    add_params: list | None = None,
    style: str = styles.LABEL,
    *,
    align: str = 'right',
    min_size: list | None = None,
    max_size: list | None = None,
):
    label = QLabel(main_layout)
    label.setText(text)
    label.setStyleSheet(style)

    if align == 'left':
        label.setAlignment(LABEL_LEFT_ALIGNMENT)
    elif align == 'right':
        label.setAlignment(LABEL_RIGHT_ALIGNMENT)

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

    return radio


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
    text: str,
    layout,
    min_size: int | list | None = None,
    max_size: int | list | None = None,
    add_layout=None,
    add_params=None,
    style: str = styles.APP_BUTTON,
    font: QFont = None,
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


def create_list(layout, style: str = styles.LIST, add_layout=None):
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


def set_button_text(button: QPushButton, text: str, max_width):
    font_metrics = QFontMetrics(button.font())
    elided_text = font_metrics.elidedText(text, Qt.ElideRight, max_width)
    button.setText(elided_text)


def set_topic_color(topic: Topic, tag: QFrame):
    if topic.color:
        if color := topic.color:
            tag.setStyleSheet(
                tag.styleSheet()
                + f'QFrame {{border-left: 2px solid {color};}} QFrame:hover {{border-left: 2px solid {color};}}'
            )


def select_tag(tag: QFrame):
    border = '2px solid rgb(70, 70, 70);'
    style = (
        f'QFrame {{border-right: {border} border-top: {border} border-bottom: {border}}}'
        if 'border-left' in tag.styleSheet()
        else f'QFrame {{border: {border}}}'
    )
    tag.setStyleSheet(tag.styleSheet() + style)


def deselect_tag(tag: QFrame):
    style = (
        'QFrame {border-right: none; border-top: none; border-bottom: none;}'
        if 'border-left' in tag.styleSheet()
        else 'QFrame {border: none;}'
    )
    tag.setStyleSheet(tag.styleSheet() + style)


def create_expand_button(
    text, layout, add_layout, add_params=None, min_size=None, max_size=None, style=EXPAND_BUTTON
):
    button = create_button(
        text,
        layout,
        min_size=min_size,
        max_size=max_size,
        add_layout=add_layout,
        add_params=add_params,
    )

    button.setIcon(QIcon(EXPAND_ICON))
    button.setIconSize(QSize(24, 24))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(style)

    menu = QMenu()

    def show_menu():
        menu.setStyleSheet(MENU)
        menu.setMinimumWidth(button.width())
        menu.setMaximumWidth(150)
        menu.popup(button.mapToGlobal(QPoint(0, button.height())))

    return button, menu, show_menu

class BorderDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        super().paint(painter, option, index)
        if color := index.data(Qt.UserRole)[1]:
            painter.setPen(QPen(QColor(color), 4))
            painter.drawLine(option.rect.topLeft(), option.rect.bottomLeft())