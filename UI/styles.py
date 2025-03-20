from UI.icons.icons import INFO_ICON, PLUS_ICON

MAIN_BUTTON = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-radius: 5px; '
    'padding-left: 10px; padding-right: 10px;} QPushButton:hover {background-color: rgb(45, 45, 45);}'
)
MAIN_WINDOW = 'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-radius: 5px;}'
MAIN_BUTTON_WITHOUT_HOVER = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-radius: 5px; '
    'padding-left: 10px; padding-right: 10px;}'
)
FILTER_BUTTON_1 = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35);'
    'border: 1px solid rgb(35, 35, 35); padding-left: 5px;}'
)
DIVIDER = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); '
    'border: 1px solid rgb(35, 35, 35); border-left: 1px solid rgb(50, 50, 50); padding: 5px;}'
)
APP_BUTTON = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35);'
    ' border: 1px solid rgb(50, 50, 50); border-radius: 5; padding: 5px;} '
)
CLEAR_BUTTON = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); padding-left: 5px; padding-right: 5px;'
    'border: 1px solid rgb(50, 50, 50); border-radius: 5;}'
    'QPushButton:hover {border: 1px solid rgb(70, 70, 70);}'
)
PICKER_BUTTON = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border: 1px solid rgb(50, 50, 50);'
    'border-radius: 5px; padding: 0px 10px, 5px, 0px; text-align: left}'
)
LABEL = 'QLabel {color: rgb(186, 189, 182); border: 0px;}'
FIELD = (
    'QLineEdit {color: rgb(186, 189, 182); border: 1px solid rgb(50, 50, 50); '
    'border-radius: 5; padding: 5px; background-color: rgb(35, 35, 35);}'
)
FOLDER_FIELD_LEFT = (
    'QLineEdit {color: rgb(186, 189, 182); border: 1px solid rgb(50, 50, 50); border-right:0px;'
    'background-color: rgb(35, 35, 35); padding: 5px; border-top-left-radius: 5; '
    'border-bottom-left-radius: 5;}'
)
FOLDER_FIELD_RIGHT = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-right: 1px solid rgb(50, 50, 50);'
    'border-bottom: 1px solid rgb(50, 50, 50); border-top: 1px solid rgb(50, 50, 50);'
    'border-top-right-radius: 5; border-bottom-right-radius: 5;'
    'padding: 6px;}'
    'QPushButton::hover {background-color: rgb(40, 40, 40);}'
)
RADIO = (
    'QRadioButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); padding-left: 10px;}'
    'QRadioButton::indicator {width: 14px; height: 14px; border: 1px solid rgb(50, 50, 50); border-radius: 8px;margin-right: 7px}'
    'QRadioButton::indicator:checked {width: 8px; height: 8px; background-color: rgb(200, 200, 200);border-radius: 8px; border: 4px solid rgb(150, 150, 150);}'
    'QRadioButton::indicator:hover {width: 14px; height: 14px; border: 1px solid rgb(70, 70, 70);}'
)


FRAME_PART = 'QFrame {background-color: rgb(35, 35, 35); border-radius: 5; border: 1px solid rgb(50, 50, 50);}'
CHECK_BOX = 'QCheckBox {color: rgb(186, 189, 182);background-color: rgb(35, 35, 35);}'
LIST = (
    'QListView {background-color: rgb(35, 35, 35)} QListView::item {color: rgb(186, 189, 182); '
    'background-color: rgb(45, 45, 45)} QListView::item:selected {background-color: rgb(40, 40, 40); color: #FFF;'
    'border-color: rgb(114, 159, 207)}'
)
FILTER_BUTTON_2 = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); '
    'border: 1px solid rgb(35, 35, 35); padding: 5px}'
)

EXIT_BUTTON = (
    'QPushButton {color: rgb(20, 20, 20); background-color: rgb(130, 130, 130); border-top-left-radius: 6;'
    'border-bottom-left-radius: 6; border-top-right-radius: 6; border-bottom-right-radius: 6;}'
)
EXIT_BUTTON_HOVER = (
    'QPushButton {color: rgb(20, 20, 20); background-color: rgb(130, 130, 130); border-top-left-radius: 6;'
    'border-bottom-left-radius: 6; border-top-right-radius: 6; border-bottom-right-radius: 6;'
    f'border-image: url({INFO_ICON}) 0 0 0 0 stretch stretch;}}'
)
SCROLLBAR = """
    QScrollBar:vertical {background-color: rgb(34, 34, 34); border-right: 1px solid rgb(50, 50, 50);
    border-bottom: 1px solid rgb(50, 50, 50); width: 10px;  margin: 0}

    QScrollBar::handle:vertical {background-color: rgb(40, 40, 40); border: 1px solid rgb(58, 58, 58);
    min-height: 5px; border-radius: 4px}

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {background: none; border: none}
    """

BLANK_SCROLLBAR = (
    'QScrollBar:vertical, QScrollBar:horizontal {width: 0px; height: 0px;}'
)

RECEIVER_LIST = """
    QListView {background-color: rgb(35, 35, 35); border-top: 1px solid rgb(50, 50, 50)}

    QListView::item {color: rgb(186, 189, 182); background-color: rgb(45, 45, 45); selection-color:rgb(255, 255, 255);
    min-height: 30px; margin-left: 5px}

    QListView::item:selected {background-color: rgb(40, 40, 40); border-color: rgb(114, 159, 207)}
    """

CLIPBOARD_LIST = """
    QListView {border-top: 1px solid rgb(50, 50, 50); border-bottom: 1px solid rgb(50, 50, 50);
    background-color: rgb(35, 35, 35);}

    QListView::item {color: rgb(186, 189, 182); background-color: rgb(45, 45, 45); min-height: 30px}

    QListView::item:selected {background-color: rgb(40, 40, 40); border-color: rgb(114, 159, 207);}
    """
X_BUTTON = """
    QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); padding: 10px; border: none;}
    QPushButton:hover {color: rgb(210, 210, 210);}
    """
WIDGET = 'QWidget {background-color: rgb(35, 35, 35); color: rgb(186, 189, 182)}'
HEADER_FRAME = 'QFrame {border-bottom: 1px solid rgb(50, 50, 50)}'
MENU = (
    'QMenu {background-color: rgb(35, 35, 35); color: rgb(186, 189, 182); border: 1px solid rgb(50, 50, 50);}'
    'QMenu::item {padding: 5px 10px;} QMenu::item:selected {background-color: rgb(45, 45, 45);}'
)
EDIT_TAG = (
    'QToolButton {background-color: rgb(45, 45, 45); border: none; border-radius: 5} '
    'QToolButton:hover {background-color: rgb(60, 60, 60);}'
)
TAG = 'QFrame {background-color: rgb(45, 45, 45); border-radius: 8; padding: 2px; border: none;}'
ADD_TAG = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-radius: 5; '
    f'border-image: url({PLUS_ICON}) 0 0 0 0 stretch stretch;}}'
)
FRAME_COLOR = 'QFrame {background: rgb(35, 35, 35); border: none;}'
COMMAND_FIELD = 'QTextEdit {background-color: rgb(26, 26, 27); color: rgb(186, 189, 182); border: 1px solid rgb(50, 50, 50);}'
DELETE_BUTTON = (
    'QPushButton {color: rgb(140, 50, 0); background-color: rgb(35, 35, 35); border: 1px solid '
    'rgb(50, 50, 50); border-radius: 5; padding: 5px;} QPushButton:hover {border: 1px solid rgb(70, 70, 70)}'
)
RECEIVER_TEXT = 'QTextEdit {color: rgb(186, 189, 182);}'
FILTER_FRAME = 'QFrame {border-top: 1px solid rgb(50, 50, 50); border-bottom: 1px solid rgb(50, 50, 50); background-color: rgb(35, 35, 35)}'
EXPAND_BUTTON = (
    'QPushButton { color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-radius: 5px; '
    'padding: 5px} QPushButton::menu-indicator { image: none; }'
)
SUCCESS_NOTIFY = (
    'QPushButton {color: rgb(255, 250, 250); background-color: rgb(103, 159, 95); border: 1px solid '
    'rgb(10, 40, 10); border-radius: 5; padding: 5px;}'
)
FAIL_NOTIFY = (
    'QPushButton {color: rgb(186, 189, 182); background-color: rgb(120, 45, 20); border: 1px solid '
    'rgb(10, 40, 10); border-radius: 5; padding: 5px;}'
)
COMMON_NOTIFY = 'QPushButton {color: rgb(186, 189, 182); background-color: rgb(45, 45, 45); border-radius: 5; padding: 5px;}'


def sidebar_button(icon_path):
    return (
        f'QPushButton {{color: rgb(186, 189, 182); background-color: rgb(30, 30, 30); border-top-left-radius: 5;'
        f'border-bottom-left-radius: 5; border-top-right-radius: 5; border-bottom-right-radius: 5; padding: 10px;'
        f'border-image: url({icon_path}) 0 0 0 0 stretch stretch;}}'
    )


def header_button(icon_path):
    return (
        f'QPushButton {{color: rgb(186, 189, 182); background-color: rgb(35, 35, 35); border-top-left-radius: 5;'
        f'border-bottom-left-radius: 5; border-top-right-radius: 5; border-bottom-right-radius: 5; padding: 10px;'
        f'border-image: url({icon_path}) 0 0 0 0 stretch stretch;}} QPushButton:hover {{background-color:'
        f' rgb(45, 45, 45);}}'
    )
