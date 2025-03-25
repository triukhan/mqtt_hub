from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QFont, QTextCharFormat, QColor

from settings.profile_manager import profile_manager


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
        if profile_manager.current_profile.convertor != 'JSON':
            return None

        self.setFormat(0, len(text), self.string_format)

        for pattern, fmt in self.rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)