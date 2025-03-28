import logging
import os
from datetime import datetime


class Logger:
    def cleanup_logs(self):
        files = sorted(
            (os.path.join(self.root, f) for f in os.listdir(self.root) if
             os.path.isfile(os.path.join(self.root, f)) and f.startswith('mqtt_sessions')),
            key=os.path.getmtime
        )
        while len(files) > int(self.max_files):
            oldest_file = files.pop(0)
            os.remove(oldest_file)
            logging.info(f'Removed old log file: {oldest_file}')

    def start_logger(self):
        if not os.path.exists(self.root):
            os.makedirs(self.root)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_filename = f'mqtt_session_{current_time}.log'
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(message)s',
            handlers=[
                logging.FileHandler(self.root + log_filename),
                logging.StreamHandler()
            ]
        )
        logging.info(f'---------------------------- Connected with result code {self.rc} ----------------------------')
        self.cleanup_logs()

    @staticmethod
    def stop_logger():
        logging.info('---------------------------- Disconnected from MQTT Client ----------------------------')
        logging.shutdown()