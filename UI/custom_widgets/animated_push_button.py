from PyQt5.QtCore import QAbstractAnimation, QVariantAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton


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
