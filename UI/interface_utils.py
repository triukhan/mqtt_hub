from enum import Enum

from PyQt5 import QtCore
from PyQt5.QtCore import (
    QAbstractAnimation,
    QPoint,
    QRegExp,
    QSize,
    Qt,
    QVariantAnimation, QRect, QTimer, QEasingCurve,
)
from PyQt5.QtGui import (
    QColor,
    QFont,
    QFontMetrics,
    QIcon,
    QPen,
    QPixmap,
    QSyntaxHighlighter,
    QTextCharFormat, QPainter,
)
from PyQt5.QtWidgets import (
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenu,
    QPushButton,
    QRadioButton,
    QScrollBar,
    QSizePolicy,
    QSpacerItem,
    QStyledItemDelegate, QStyleOptionViewItem, QStyle, QAbstractItemView,
)
from qtwidgets import AnimatedToggle

from settings.topic import Topic
from UI import styles
from UI.icons.icons import EXPAND_ICON, EDIT_ICON
from UI.styles import EXPAND_BUTTON, MENU, SCROLLBAR, CLIPBOARD_LIST

LABEL_RIGHT_ALIGNMENT = (
    QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
)
LABEL_LEFT_ALIGNMENT = QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter


class Spacer(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


FONT = QFont()
FONT.setPointSize(10)


class AnimatedPushButton(QPushButton):
    def __init__(self, parent=None, style=None):
        super().__init__(parent)
        self.base_style = style or ''
        self._animation = QVariantAnimation(
            startValue=QColor('#323232'),
            endValue=QColor('#464646'),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QColor('#444444'))

    def _on_value_changed(self, border_color):
        self._update_stylesheet(border_color)

    def _update_stylesheet(self, border_color):
        updated_style = self.base_style.replace(
            'border: 1px solid rgb(50, 50, 50);',
            f'border: 1px solid {border_color.name()};',
        )
        self.setStyleSheet(updated_style)

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().leaveEvent(event)


class AnimatedLineEdit(QLineEdit):
    def __init__(self, parent=None, style=None):
        super().__init__(parent)
        self.base_style = style or ''
        self.focused = False
        self._animation = QVariantAnimation(
            startValue=QColor('#323232'),
            endValue=QColor('#444444'),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QColor('#323232'))

    def _on_value_changed(self, border_color):
        self._update_stylesheet(border_color)

    def _update_stylesheet(self, border_color):
        updated_style = self.base_style.replace(
            'border: 1px solid rgb(50, 50, 50);',
            f'border: 1px solid {border_color.name()};',
        )
        self.setStyleSheet(updated_style)

    def focusInEvent(self, event):
        self.focused = True
        self._update_stylesheet(QColor('#444444'))
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.focused = False
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().focusOutEvent(event)

    def enterEvent(self, event):
        if not self.focused:
            self._animation.setDirection(QAbstractAnimation.Forward)
            self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if not self.focused:
            self._animation.setDirection(QAbstractAnimation.Backward)
            self._animation.start()
        super().leaveEvent(event)


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
):
    field = AnimatedLineEdit(main_layout, style)
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
    toggle = AnimatedToggle(
        handle_color=Qt.gray,
        bar_color=Qt.darkGray,
        checked_color=Qt.darkGray,
        pulse_checked_color='#44999999',
    )
    toggle.setFixedWidth(55)
    toggle.setFixedHeight(40)

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
    border=True,
):
    button = AnimatedPushButton(layout, style) if border else QPushButton(layout)
    button.setText(text)
    button.setStyleSheet(style)

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
    field = create_field(frame, layout, style=styles.FOLDER_FIELD_LEFT)
    button = create_button(
        '', frame, add_layout=layout, style=styles.FOLDER_FIELD_RIGHT
    )

    icon_folder = QIcon()
    icon_folder.addPixmap(QPixmap('UI/icons/folder-icon.svg'), QIcon.Normal, QIcon.Off)
    button.setIcon(icon_folder)

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
    text,
    layout,
    add_layout,
    add_params=None,
    min_size=None,
    max_size=None,
    style=EXPAND_BUTTON,
    border=True,
):
    button = create_button(
        text,
        layout,
        min_size=min_size,
        max_size=max_size,
        add_layout=add_layout,
        add_params=add_params,
        style=style,
        border=border,
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


class JsonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.font = QFont('Monospace', 8)
        self.font.setStyleHint(QFont.TypeWriter)

        self.int_format = QTextCharFormat()
        self.int_format.setForeground(QColor('#9de67e'))
        self.int_format.setFont(self.font)

        self.key_format = QTextCharFormat()
        self.key_format.setForeground(QColor('#82c9f1'))
        self.key_format.setFont(self.font)

        self.string_format = QTextCharFormat()
        self.string_format.setForeground(QColor('#e48368'))
        self.string_format.setFont(self.font)

        self.bool_format = QTextCharFormat()
        self.bool_format.setForeground(QColor('#d077d6'))
        self.bool_format.setFont(self.font)

        self.common_format = QTextCharFormat()
        self.common_format.setForeground(QColor('#c0c0c0'))
        self.common_format.setFont(self.font)

        self.rules = [
            (QRegExp(r'"([^"]+)":'), self.key_format),
            (QRegExp(r'\b(true|false)\b'), self.bool_format),
            (QRegExp(r':\s*(\d+)\b(?!")'), self.int_format),
            (QRegExp(r'[\[\]{}]'), self.common_format),
            (QRegExp(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'), self.common_format),
            (QRegExp(r',\s*$'), self.common_format),
        ]

    def highlightBlock(self, text):
        self.setFormat(0, len(text), self.string_format)

        for pattern, fmt in self.rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)

class RightButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.icon = QPixmap(EDIT_ICON).scaled(
            24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.button_rects = {}
        self.hovered_row = -1
        self.opacity_values = {}
        self.animations = {}

        self.timer = QTimer()
        self.timer.timeout.connect(self.parent.viewport().update)

    def paint(self, painter: QPainter, option, index):
        text = index.data(Qt.DisplayRole)
        rect = option.rect
        padding = 5
        icon_size = self.icon.size()

        if option.state & QStyle.State_Selected:
            painter.fillRect(rect, QColor(40, 40, 40))
        else:
            painter.fillRect(rect, QColor(45, 45, 45))

        painter.setPen(QColor(186, 189, 182))
        text_rect = rect.adjusted(5, 0, -icon_size.width() - padding, 0)
        painter.drawText(text_rect, Qt.AlignVCenter, text)

        row = index.row()
        opacity = self.opacity_values.get(row, 0.0)

        if opacity > 0:
            icon_x = rect.right() - icon_size.width() - padding
            icon_y = rect.center().y() - icon_size.height() // 2
            button_rect = QRect(icon_x, icon_y, icon_size.width(), icon_size.height())

            self.button_rects[row] = button_rect
            painter.setOpacity(opacity)
            painter.drawPixmap(button_rect, self.icon)
            painter.setOpacity(1)

    def setHoveredRow(self, row):
        if self.hovered_row != row:
            previous_row = self.hovered_row
            self.hovered_row = row

            if row != -1:
                self.startOpacityAnimation(row, 1.0)
            if previous_row != -1 and previous_row != row:
                self.startOpacityAnimation(previous_row, 0.0)

    def startOpacityAnimation(self, row, target_opacity):
        start_opacity = self.opacity_values.get(row, 0.0)

        if row in self.animations:
            self.animations[row].stop()

        animation = QVariantAnimation()
        animation.setDuration(300)
        animation.setStartValue(start_opacity)
        animation.setEndValue(target_opacity)
        animation.valueChanged.connect(lambda value: self.updateOpacity(row, value))

        self.animations[row] = animation
        animation.start()

    def updateOpacity(self, row, value):
        self.opacity_values[row] = value
        self.parent.viewport().update()

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonPress:
            row = index.row()
            if row in self.button_rects and self.button_rects[row].contains(event.pos()):
                print(f'Clicked row {row}!')
                return True
        return False


class ClipboardListWidget(QListWidget):
    def __init__(self, layout):
        super().__init__(layout)
        self.setMouseTracking(True)
        self.delegate = RightButtonDelegate( self)
        self.setItemDelegate(self.delegate)
        self.setStyleSheet(CLIPBOARD_LIST)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setMinimumSize(220, 0)
        self.setMaximumSize(16777215, 16777215)
        self.setFrameShape(QFrame.NoFrame)

    def mouseMoveEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid():
            self.delegate.setHoveredRow(index.row())
        else:
            self.delegate.setHoveredRow(-1)

    def leaveEvent(self, event):
        self.delegate.setHoveredRow(-1)
