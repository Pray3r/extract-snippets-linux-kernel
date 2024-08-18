import logging
import json

class LoggerManager:
    def __init__(self, name, log_file, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_json(self, message, data, level=logging.INFO):
        log_entry = {"message": message, "data": data}
        log_entry_json = json.dumps(log_entry)
        self.logger.log(level, log_entry_json)
