from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

from settings.profile_manager import profile_manager
from UI import styles
from UI.custom_widgets.clipboard_list import ClipboardListWidget
from UI.interface_utils import (
    Spacer,
    create_button,
    create_expand_button,
    create_frame,
    create_label,
    create_layout,
    create_list,
    create_scroll_bar,
    create_spacer,
    create_toggle, create_text_edit,
)
from UI.styles import (
    CLEAR_BUTTON,
    COMMAND_FIELD,
    FILTER_FRAME,
    FRAME_COLOR,
    RECEIVER_TEXT,
)


class MainTabUI(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout_2 = create_layout(QGridLayout, [0, 0, 0, 0], 0, out_layout=self)
        self.main_right_layout = create_layout(QVBoxLayout, [0, -1, 0, 0], 0)

        self.clear_frame = create_frame(
            self,
            FRAME_COLOR,
            add_layout=self.main_right_layout,
        )
        self.clear_layout = create_layout(
            QHBoxLayout, [10, 12, 10, 10], 10, out_layout=self.clear_frame
        )

        self.autoscroll_toggle = create_toggle(self.clear_layout)
        self.autoscroll_label = create_label(
            'Autoscroll',
            self.clear_frame,
            self.clear_layout,
            style=styles.LABEL + 'QLabel {margin-bottom: 2px}',
        )
        self.clear_layout.addItem(create_spacer(Spacer.HORIZONTAL))
        font = QFont()
        font.setPointSize(10)
        self.clear_button = create_button(
            'clear',
            self.clear_frame,
            max_size=[50, 18],
            add_layout=self.clear_layout,
            style=CLEAR_BUTTON,
            font=font,
        )

        self.receiver_list = create_list(
            self, styles.RECEIVER_LIST, self.main_right_layout
        )
        create_scroll_bar(self, self.receiver_list)

        self.filter_frame = create_frame(
            self,
            FILTER_FRAME,
            add_layout=self.main_right_layout,
        )
        self.message_formating = create_layout(
            QHBoxLayout, [12, 5, 0, 5], 0, out_layout=self.filter_frame
        )

        self.convertor_button, self.convert_menu, self.show_convert_menu = (
            create_expand_button(
                profile_manager.current_profile.convertor,
                self.filter_frame,
                min_size=[100, 25],
                max_size=[100, 25],
                style=styles.PICKER_BUTTON,
                add_layout=self.message_formating,
            )
        )

        self.message_formating.addItem(create_spacer(Spacer.HORIZONTAL))

        self.select_label = create_label(
            'Select Message  ',
            self.filter_frame,
            min_size=[110, 23],
            max_size=[110, 23],
            add_layout=self.message_formating,
        )

        self.select_toggle = create_toggle(self.message_formating)

        self.receiver_text_edit = create_text_edit(self, style=RECEIVER_TEXT, add_layout=self.main_right_layout)
        self.receiver_text_edit.setReadOnly(True)
        self.receiver_text_edit.setFrameShape(QFrame.NoFrame)
        create_scroll_bar(self, self.receiver_text_edit)

        self.gridLayout_2.addLayout(self.main_right_layout, 0, 1, 1, 1)

        self.main_left_layout = QFrame(self)

        self.verticalLayout_3 = create_layout(
            QVBoxLayout, margins=0, out_layout=self.main_left_layout
        )

        self.publisher_head_frame = create_frame(
            self.main_left_layout, style=FRAME_COLOR
        )

        self.horizontalLayout_5 = create_layout(
            QHBoxLayout, 15, 20, out_layout=self.publisher_head_frame
        )

        (
            self.clipboard_convertor_button,
            self.convert_clipboard_menu,
            self.show_clipboard_convert_menu,
        ) = create_expand_button(
            profile_manager.current_profile.clipboard_convertor,
            self.publisher_head_frame,
            min_size=[0, 25],
            max_size=[100, 25],
            style=styles.PICKER_BUTTON,
            add_layout=self.horizontalLayout_5,
        )

        self.add_clipboard_button = create_button(
            'Add to Clipboard',
            self.publisher_head_frame,
            [0, 25],
            [150, 25],
            self.horizontalLayout_5,
            style=styles.APP_BUTTON,
        )

        self.publish_button = create_button(
            'Publish',
            self.publisher_head_frame,
            min_size=[0, 25],
            max_size=[150, 25],
            add_layout=self.horizontalLayout_5,
        )

        self.verticalLayout_3.addWidget(self.publisher_head_frame)
        self.clipboard_layout = create_layout(QHBoxLayout, [-1, -1, 1, -1])

        self.clipboard_list = ClipboardListWidget(self.main_left_layout)
        self.clipboard_layout.addWidget(self.clipboard_list)

        self.command_field = create_text_edit(self.main_left_layout, style=COMMAND_FIELD, add_layout=self.clipboard_layout)
        self.command_field.setFrameShape(QFrame.NoFrame)
        self.clipboard_layout.setStretch(0, 1)
        self.clipboard_layout.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.clipboard_layout)
        self.bottom_frame = QWidget(self.main_left_layout)
        self.bottom_frame.setFixedHeight(0)
        self.gridLayout_2.addWidget(self.main_left_layout, 0, 0, 1, 1)
