from PyQt5.QtCore import QAbstractAnimation, QVariantAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton


class AnimatedPushButton(QPushButton):
    def __init__(
        self,
        parent=None,
        style=None,
        body=False,
        start_value: set = None,
        end_value: set = None,
    ):
        super().__init__(parent)
        self.body = body
        self.start_value = start_value
        self.start_color = (
            QColor('#323232' if not self.body else '#1e1e1e')
            if start_value is None
            else QColor(*start_value)
        )
        self.end_color = (
            QColor('#464646' if not self.body else '#282828')
            if end_value is None
            else QColor(*end_value)
        )
        self.selected = False

        self._animation = QVariantAnimation(
            startValue=self.start_color,
            endValue=self.end_color,
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._initial_style = style or ''

    def _on_value_changed(self, color):
        self._update_stylesheet(color)

    def _update_stylesheet(self, color):
        if not self.isEnabled():
            return

        if self.body:
            if self.selected:
                return
            updated_style = self._initial_style.replace(
                f'background-color: rgb{str(self.start_value) if self.start_value else '(30, 30, 30)'}',
                f'background-color: {color.name()}',
            )
        else:
            updated_style = self._initial_style.replace(
                'border: 1px solid rgb(50, 50, 50);',
                f'border: 1px solid {color.name()};',
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

    def select(self):
        self.setStyleSheet(
            self.styleSheet() + 'QPushButton {background-color: rgb(40, 40, 40);}'
        )
        self.selected = True

    def deselect(self):
        self.setStyleSheet(
            self.styleSheet() + 'QPushButton {background-color: rgb(30, 30, 30);}'
        )
        self.selected = False
