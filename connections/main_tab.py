from GUI.tabs.main_tab import MainTabUI
from settings.profile_manager import ProfileManager


class PlusTab(MainTabUI):
    def __init__(self):
        super().__init__()
        self.profile_manager = ProfileManager()
        self.current_profile = self.profile_manager.current_profile
