from GUI.main_window import MqttHubUi
from settings.profile_manager import ProfileManager


class MainWindow(MqttHubUi):
    def __init__(self):
        super().__init__()
        self.profile_manager = ProfileManager()
        self.current_profile = self.profile_manager.current_profile

    # def connect
