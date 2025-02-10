from GUI.tabs.main_tab_gui import MainTabUI


class MainTab(MainTabUI):
    def __init__(self):
        super().__init__()

    def get_command_text(self):
        self.command_field.toPlainText()
