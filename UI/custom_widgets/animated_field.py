from PyQt5.QtCore import QAbstractAnimation, QVariantAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLineEdit


class AnimatedLineEdit(QLineEdit):
    def __init__(self, parent=None, style=None, button=None):
        super().__init__(parent)
        self.base_style = style or ''
        self.focused = False
        self.button = button
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
        if self.isReadOnly():
            return
        updated_style = self.base_style.replace(
            'border: 1px solid rgb(50, 50, 50);',
            f'border: 1px solid {border_color.name()};',
        )
        self.setStyleSheet(updated_style)

    def start_hover_animation(self, forward=True):
        self._animation.setDirection(
            QAbstractAnimation.Forward if forward else QAbstractAnimation.Backward
        )
        self._animation.start()

        if self.button:
            self.button._animation.setDirection(
                QAbstractAnimation.Forward if forward else QAbstractAnimation.Backward
            )
            self.button._animation.start()

    def focusInEvent(self, event):
        self.focused = True
        self.start_hover_animation(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.focused = False
        self.start_hover_animation(False)
        super().focusOutEvent(event)

    def enterEvent(self, event):
        if not self.focused:
            self.start_hover_animation(True)
        super().enterEvent(event)

    def leaveEvent(self, event):
        if not self.focused:
            self.start_hover_animation(False)
        super().leaveEvent(event)
