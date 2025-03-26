import re

from PyQt5.QtCore import QAbstractAnimation, QPoint, QRect, QSize, QVariantAnimation
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QToolButton,
)

from settings.profile_manager import profile_manager
from settings.topic import Topic
from UI.icons.icons import EDIT_ICON
from UI.interface_utils import (
    create_button,
    create_label,
    create_layout,
    set_topic_color,
)
from UI.styles import ADD_TAG, EDIT_TAG, FRAME_COLOR, TAG, TAG_LABEL


class FlowLayout(QLayout):
    def __init__(self, parent=None, spacing=5):
        super().__init__(parent)
        self.item_list = []
        self._spacing = spacing

    def addItem(self, item):
        self.item_list.append(item)
        self.invalidate()

    def itemAt(self, index):
        if index < 0 or index >= len(self.item_list):
            return None
        return self.item_list[index]

    def insertWidget(self, index, widget):
        self.addWidget(widget)
        self.item_list.insert(index, self.item_list.pop(-1))
        self.invalidate()

    def removeWidget(self, widget):
        if widget in [item.widget() for item in self.item_list]:
            widget.deleteLater()
            self.item_list = [
                item for item in self.item_list if item.widget() != widget
            ]
            self.invalidate()

    def count(self):
        return len(self.item_list)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize(0, 0)
        for item in self.item_list:
            size = size.expandedTo(item.sizeHint())
        return size + QSize(2 * self._spacing, 2 * self._spacing)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        x, y, rowHeight = rect.x(), rect.y(), 0
        for item in self.item_list:
            next_x = x + item.sizeHint().width() + self._spacing
            if next_x > rect.right() and rowHeight > 0:
                x = rect.x()
                y += rowHeight + self._spacing
                next_x = x + item.sizeHint().width() + self._spacing
                rowHeight = 0
            item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
            x = next_x
            rowHeight = max(rowHeight, item.sizeHint().height())

        if self.item_list:
            last_item = self.item_list[-1]
            if (
                isinstance(last_item.widget(), QPushButton)
                and last_item.widget().text() == ''
            ):
                last_item.setGeometry(QRect(QPoint(x - 40, y), last_item.sizeHint()))


class TagsWidget(QFrame):
    def __init__(self, parent=None, edit_method=None):
        super().__init__(parent)
        self.edit_method = edit_method
        self.selected_tag = None

        self.setFixedHeight(100)
        self.setStyleSheet(FRAME_COLOR)
        self.setContentsMargins(10, 10, 0, 0)

        self.tags_layout = FlowLayout(self, spacing=10)
        self.setLayout(self.tags_layout)

        self.add_button = create_button(
            '',
            self,
            style=ADD_TAG,
            min_size=30,
            max_size=30,
            body=True,
            start_value=(35, 35, 35),
            end_value=(45, 45, 45),
        )
        self.add_button.setProperty('add_button', True)
        self.tags_layout.addWidget(self.add_button)

    def add_tag(self, topic: Topic):
        tag = AnimatedTagFrame(self)
        set_topic_color(topic, tag)
        tag.setFixedSize(115, 30)
        tag_layout = create_layout(QHBoxLayout, 0, 0, tag)

        tag_label = create_label(topic.get_name(), tag, align='left', style=TAG_LABEL)
        tag_label.setFixedWidth(90)
        tag_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )

        icon_button = QToolButton(tag)
        icon_button.setFixedSize(22, 22)
        icon_button.setStyleSheet(EDIT_TAG)
        icon_button.clicked.connect(
            lambda: self.edit_method(topic, {'frame': tag, 'label': tag_label})
        )

        tag_layout.addWidget(tag_label)
        tag_layout.addWidget(icon_button)
        tag.setLayout(tag_layout)
        tag.setProperty('address', topic.address)

        tag.mousePressEvent = lambda event: self.select_tag(tag, topic)
        self.tags_layout.insertWidget(self.tags_layout.count() - 1, tag)

    def select_tag(self, tag, topic):
        if self.selected_tag:
            self.selected_tag.deselect()

        self.selected_tag = tag
        self.selected_tag.select()
        profile_manager.topic_to_publish = topic

    def remove_tag(self, tag):
        self.tags_layout.removeWidget(tag)

    def clear_tags(self):
        for i in range(self.tags_layout.count() - 1, -1, -1):
            item = self.tags_layout.itemAt(i)
            if item:
                tag_frame = item.widget()
                if tag_frame.property('add_button'):
                    continue
                self.remove_tag(tag_frame)

    def find_tag_by_address(self, address):
        for i in range(self.tags_layout.count() - 1, -1, -1):
            item = self.tags_layout.itemAt(i)
            if item:
                tag_frame = item.widget()
                if tag_frame.property('address') == address:
                    return tag_frame

    def remove_tag_by_address(self, address):
        tag = self.find_tag_by_address(address)
        self.remove_tag(tag)
        profile_manager.topic_to_publish = None
        self.selected_tag = None


class AnimatedTagFrame(QFrame):
    def __init__(self, parent=None, start_color=(50, 50, 50), end_color=(80, 80, 80)):
        super().__init__(parent)
        self.start_color = QColor(*start_color)
        self.end_color = QColor(*end_color)
        self.selected = False

        self._animation = QVariantAnimation(
            startValue=self.start_color,
            endValue=self.end_color,
            valueChanged=self._on_value_changed,
            duration=400,
        )

        self._initial_style = TAG
        self.setStyleSheet(self._initial_style)

    def _on_value_changed(self, color):
        self._update_stylesheet(color)

    def _update_stylesheet(self, color):
        border_left = re.findall(
            r'QFrame\s*{\s*border-left:\s*2px\s*solid\s*#[0-9A-Fa-f]{6}\s*;?\s*}',
            self.styleSheet(),
        )
        border_left = border_left[0] if len(border_left) > 0 else ''
        updated_style = (
            self.styleSheet()
            + f'QFrame {{border: 1px solid {color.name()}}}'
            + border_left
        )
        self.setStyleSheet(updated_style)

    def enterEvent(self, event):
        if not self.selected:
            self._animation.setDirection(QAbstractAnimation.Forward)
            self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if not self.selected:
            self._animation.setDirection(QAbstractAnimation.Backward)
            self._animation.start()
        super().leaveEvent(event)

    def select(self):
        self.selected = True
        border = '2px solid rgb(70, 70, 70);'
        style = (
            f'QFrame {{border-right: {border} border-top: {border} border-bottom: {border}}}'
            if 'border-left' in self.styleSheet()
            else f'QFrame {{border: {border}}}'
        )
        self.setStyleSheet(self.styleSheet() + style)

    def deselect(self):
        self.selected = False
        style = (
            'QFrame {border-right: none; border-top: none; border-bottom: none;}'
            if 'border-left' in self.styleSheet()
            else 'QFrame {border: none;}'
        )
        self.setStyleSheet(self.styleSheet() + style)
