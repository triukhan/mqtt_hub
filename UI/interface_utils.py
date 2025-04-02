import platform
import re
from enum import Enum

from PyQt5 import QtCore
from PyQt5.QtCore import (
    QEasingCurve,
    QPoint,
    QPropertyAnimation,
    QRect,
    QSize,
    Qt,
    pyqtProperty,
)
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QFont,
    QFontMetrics,
    QIcon,
    QPainter,
    QPainterPath,
    QPen,
    QPixmap,
)
from PyQt5.QtWidgets import (
    QAction,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMenu,
    QPushButton,
    QRadioButton,
    QScrollBar,
    QSizePolicy,
    QSpacerItem,
    QStyledItemDelegate,
    QTextEdit,
)

from settings.profile_manager import profile_manager
from settings.topic import Topic
from UI import styles
from UI.custom_widgets.animated_field import AnimatedLineEdit
from UI.custom_widgets.animated_push_button import AnimatedPushButton
from UI.custom_widgets.animated_spin import AnimatedSpinBox
from UI.custom_widgets.toggle import QToggle
from UI.icons.icons import EXPAND_ICON
from UI.styles import (
    EXPAND_BUTTON,
    MAIN_BUTTON_WITHOUT_HOVER,
    MENU,
    SCROLLBAR,
    TEXT_EDIT,
)

LABEL_RIGHT_ALIGNMENT = (
    QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
)
LABEL_LEFT_ALIGNMENT = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter


class Spacer(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


FONT = QFont()
FONT.setPointSize(10)


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
    elif align == 'center':
        label.setAlignment(Qt.AlignCenter)

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


def create_field(
    main_layout,
    add_layout=None,
    add_params: list | None = None,
    style: str = styles.FIELD,
    button=None,
    spinbox=False,
):
    if spinbox:
        field = AnimatedSpinBox(main_layout, style)
        field.setStyleSheet(style)
    else:
        field = AnimatedLineEdit(main_layout, style, button)
        field.setStyleSheet(style)

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


def create_toggle(add_layout=None, add_params: list | None = None):
    toggle = QToggle()
    toggle.bg_color = QColor('#787878')
    toggle.active_color = QColor('#50ab4f')

    if add_params:
        add_layout.addWidget(toggle, *add_params)
    else:
        add_layout.addWidget(toggle)

    return toggle


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
    layout_type,
    margins: list | int | None = None,
    spacing: int = 0,
    out_layout=None,
    align=None,
):
    if out_layout is not None:
        layout = layout_type(out_layout)
    else:
        layout = layout_type()

    if isinstance(margins, int):
        margins = [margins for _ in range(4)]

    if align is not None:
        layout.setAlignment(align)

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
    anim: bool = True,
    body: bool = False,
    start_value: tuple | None = None,
    end_value: tuple | None = None,
    icon: str | None = None,
):
    if icon is not None and platform.system() == 'Linux':
        pattern = r'border-image:\s*url\([^)]+\)\s*\d+\s+\d+\s+\d+\s+\d+\s+stretch\s+stretch;'
        style = re.sub(pattern, '', style)

    button = (
        AnimatedPushButton(layout, style, body, start_value, end_value)
        if anim
        else QPushButton(layout)
    )
    button.setText(text)
    button.setStyleSheet(style)

    if icon is not None and platform.system() == 'Linux':
        button.setIcon(QIcon(icon))
        button.setIconSize(QSize(30, 30))

    if font is not None:
        button.setFont(font)

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


def create_scroll_bar(obj, layout, style=SCROLLBAR):
    scroll_bar = QScrollBar(obj)
    scroll_bar.setStyleSheet(style)
    layout.setVerticalScrollBar(scroll_bar)


def create_folder_field(frame, add_layout, add_params: list):
    layout = create_layout(QHBoxLayout, spacing=0)
    button = create_button(
        '', frame, style=styles.FOLDER_FIELD_RIGHT, max_size=[30, 30]
    )
    field = create_field(frame, style=styles.FOLDER_FIELD_LEFT, button=button)

    icon_folder = QIcon()
    icon_folder.addPixmap(QPixmap('UI/icons/folder-icon.svg'), QIcon.Normal, QIcon.Off)
    button.setIcon(icon_folder)

    layout.addWidget(field)
    layout.addWidget(button)
    add_layout.addLayout(layout, *add_params)

    return field, button


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


def create_expand_button(
    text,
    layout,
    add_layout,
    add_params=None,
    min_size=None,
    max_size=None,
    style=EXPAND_BUTTON,
    body=False,
    start_value=None,
    end_value=None,
):
    button = create_button(
        text,
        layout,
        min_size=min_size,
        max_size=max_size,
        add_layout=add_layout,
        add_params=add_params,
        style=style,
        body=body,
        start_value=start_value,
        end_value=end_value,
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


def create_text_edit(frame, min_height=None, style=TEXT_EDIT, add_layout=None):
    text_edit = QTextEdit(frame)
    text_edit.setStyleSheet(style)

    if min_height is not None:
        text_edit.setMinimumHeight(min_height)
    if add_layout is not None:
        add_layout.addWidget(text_edit)
    return text_edit


def create_convert_menu(button, menu, formats, callback):
    font_metrics = QFontMetrics(button.font())

    for convert_format in formats:
        elided_text = font_metrics.elidedText(convert_format, Qt.ElideRight, 110)
        action = QAction(elided_text, button)
        action.triggered.connect(lambda _, f=convert_format: callback(f))
        menu.addAction(action)


class BorderDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        super().paint(painter, option, index)
        if (color := index.data(Qt.UserRole)[1]) == '':
            color = '#2d2d2d'
        painter.setPen(QPen(QColor(color), 4))
        painter.drawLine(option.rect.topLeft(), option.rect.bottomLeft())


def create_profile_button(text, layout, add_layout, add_params: list, set_profile):
    button, menu, show_menu = create_expand_button(
        text,
        layout,
        min_size=[0, 30],
        max_size=[200, 30],
        add_layout=add_layout,
        add_params=add_params,
        style=MAIN_BUTTON_WITHOUT_HOVER,
        body=True,
        start_value=(35, 35, 35),
        end_value=(45, 45, 45),
    )

    profiles = profile_manager.profiles
    for _, profile in profiles.items():
        if profile.is_default != 'None':
            continue
        font_metrics = QFontMetrics(button.font())
        elided_text = font_metrics.elidedText(profile.name, Qt.ElideRight, 110)

        action = QAction(elided_text, button)
        action.triggered.connect(lambda _, p=profile: set_profile(p))
        menu.addAction(action)

    button.clicked.connect(show_menu)

    return button
