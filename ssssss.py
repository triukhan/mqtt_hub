from PyQt5.QtCore import QVariantAnimation, Qt, QAbstractAnimation
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtWidgets import QPushButton, QDialog, QSizePolicy, QVBoxLayout, QApplication

from PyQt5.QtCore import QVariantAnimation, Qt, QAbstractAnimation
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtWidgets import QLineEdit, QApplication, QVBoxLayout, QWidget


class AnimatedLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("#444444"),  # Темно-серый бордер
            endValue=QColor("#4CAF50"),    # Зеленый при фокусе
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QColor("#444444"))  # Устанавливаем начальный бордер

    def _on_value_changed(self, border_color):
        self._update_stylesheet(border_color)

    def _update_stylesheet(self, border_color):
        self.setStyleSheet(
            f"""
        QLineEdit {{
            background-color: white;
            color: black;
            padding: 8px;
            font-size: 16px;
            border: 2px solid {border_color.name()};
            border-radius: 4px;
        }}
        """
        )

    def focusInEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().focusOutEvent(event)

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().leaveEvent(event)





class PushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("#444444"),
            endValue=QColor("#4CAF50"),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QColor("#444444"))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, border_color):
        self._update_stylesheet(border_color)

    def _update_stylesheet(self, border_color):
        self.setStyleSheet(
            f"""
        QPushButton {{
            background-color: white;  /* Фон остается белым */
            color: black;
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            margin: 4px 2px;
            border: 2px solid {border_color.name()};
        }}
        """
        )

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().leaveEvent(event)




class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle(self.tr("Dialog"))

        self.pushButton = PushButton()
        self.pushButton.setText(self.tr("Click Here"))
        self.pushButton.setSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Minimum
        )

        self.line_edit = AnimatedLineEdit(self)

        lay = QVBoxLayout(self)
        lay.addWidget(self.pushButton)
        lay.addWidget(self.line_edit)

        self.resize(400, 300)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())