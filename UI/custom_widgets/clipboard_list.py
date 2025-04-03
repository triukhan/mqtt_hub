from PyQt5.QtCore import QRect, QRectF, Qt, QTimer, QVariantAnimation, QEvent
from PyQt5.QtGui import QColor, QDrag, QPainter, QPainterPath, QPixmap
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QFrame,
    QListWidget,
    QStyle,
    QStyledItemDelegate,
)

from settings.profile_manager import profile_manager
from UI.icons.icons import EDIT_ICON
from UI.styles import CLIPBOARD_LIST


class RightButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent, method):
        super().__init__(parent)
        self.parent = parent
        self.icon = QPixmap(EDIT_ICON).scaled(
            24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.button_rects = {}
        self.hovered_row = -1
        self.hovered_button_row = -1
        self.opacity_values = {}
        self.animations = {}
        self.method = method

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

            if self.hovered_button_row == row:
                rounded_path = QPainterPath()
                rounded_path.addRoundedRect(QRectF(button_rect), 6, 6)
                painter.setRenderHint(QPainter.Antialiasing)
                painter.fillPath(rounded_path, QColor(40, 40, 40))

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
            if row in self.button_rects and self.button_rects[row].contains(
                event.pos()
            ):
                self.method(index)
                return True
        return False


class ClipboardListWidget(QListWidget):
    def __init__(self, layout):
        super().__init__(layout)
        self._setup_preferences()
        self.delegate = RightButtonDelegate(self, None)
        self.setItemDelegate(self.delegate)
        self.drag_start_pos = None
        self.click_timer = QTimer(self)
        self.click_timer.setSingleShot(True)
        self.click_timer.timeout.connect(self.handle_click)

    def set_method(self, method):
        self.delegate.method = method

    def _setup_preferences(self):
        self.setMouseTracking(True)
        self.setStyleSheet(CLIPBOARD_LIST)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setMinimumSize(220, 0)
        self.setMaximumSize(16777215, 16777215)
        self.setFrameShape(QFrame.NoFrame)

    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())

        if index.isValid():
            super().mousePressEvent(event)

            if event.button() == Qt.LeftButton:
                self.drag_start_pos = event.pos()
                self.click_timer.start(50)

        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.drag_start_pos:
            if (event.pos() - self.drag_start_pos).manhattanLength() > QApplication.startDragDistance():
                self.drag_start_pos = None
                drag = QDrag(self)
                mime_data = self.model().mimeData(self.selectedIndexes())
                drag.setMimeData(mime_data)
                drag.exec_(Qt.MoveAction)
        index = self.indexAt(event.pos())
        if index.isValid():
            row = index.row()
            self.delegate.setHoveredRow(row)

            if row in self.delegate.button_rects and self.delegate.button_rects[
                row
            ].contains(event.pos()):
                if self.delegate.hovered_button_row != row:
                    self.delegate.hovered_button_row = row
                    self.viewport().update()
            else:
                if self.delegate.hovered_button_row != -1:
                    self.delegate.hovered_button_row = -1
                    self.viewport().update()
        else:
            self.delegate.setHoveredRow(-1)
            self.delegate.hovered_button_row = -1
            self.viewport().update()

        super().mouseMoveEvent(event)

    def handle_click(self):
        self.drag_start_pos = None


    def leaveEvent(self, event):
        self.delegate.setHoveredRow(-1)
        self.delegate.hovered_button_row = -1
        self.viewport().update()

    def dropEvent(self, event):
        super().dropEvent(event)
        self.update_config()

    def update_config(self):
        profile_manager.current_profile.clear_clipboard()

        for item in range(self.count()):
            item = self.item(item)
            msg_text, msg_id = item.data(Qt.UserRole)
            msg_name = msg_id[: msg_id.find('_id_starts_here')]
            profile_manager.current_profile.add_clipboard(msg_name, msg_text)
