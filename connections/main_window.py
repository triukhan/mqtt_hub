from GUI.main_window import MqttHubUi
from settings.profile_manager import ProfileManager


class MainWindow(MqttHubUi):
    def __init__(self):
        super().__init__()
        self.profile_manager = ProfileManager()
        self.current_profile = self.profile_manager.current_profile
        self.setup_ui()
        self.main_button.clicked.connect(self.open_main_tab)
        self.plus_button.clicked.connect(self.open_plus_tab)
        self.exit_button.clicked.connect(self.close)
        self.settings_button.clicked.connect(self.open_settings_tab)
        self.info_button.clicked.connect(self.open_info_tab)

    def open_main_tab(self):
        self.all_tabs.setCurrentIndex(0)
        self.setup_main_header()

    def open_plus_tab(self):
        self.all_tabs.setCurrentIndex(1)
        self.setup_plus_header()

    def open_edit_tab(self):
        self.all_tabs.setCurrentIndex(2)
        self.setup_edit_header()

    def open_settings_tab(self):
        self.all_tabs.setCurrentIndex(3)

    def open_info_tab(self):
        self.all_tabs.setCurrentIndex(4)
