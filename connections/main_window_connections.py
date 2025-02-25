from GUI.main_window_gui import MqttHubUi
from settings.profile_manager import profile_manager


class MainWindow(MqttHubUi):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        self.connect_sidebar()
        self.main_tab.setup_topics()
        self.update_profile_button()

    @property
    def current_profile(self):
        return profile_manager.current_profile

    def save_new_profile(self):
        settings = self.plus_tab.get_settings()
        profile_manager.create_profile(**settings)
        self.open_main_tab()

    def open_main_tab(self):
        self.all_tabs.setCurrentIndex(0)
        self.setup_main_header()
        self.update_profile_button()

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

    def connect_sidebar(self):
        self.main_button.clicked.connect(self.open_main_tab)
        self.plus_button.clicked.connect(self.open_plus_tab)
        self.settings_button.clicked.connect(self.open_settings_tab)
        self.info_button.clicked.connect(self.open_info_tab)
        self.exit_button.clicked.connect(self.close)

    def update_profile_button(self):
        self.profile_button.setText(self.current_profile.name)
