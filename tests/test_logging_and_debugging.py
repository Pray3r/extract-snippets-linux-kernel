import unittest
import os
from src.utils.logging.logger_manager import LoggerManager

class TestLoggingAndDebugging(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_logging.log"
        self.logger = LoggerManager("test_logger", self.log_file).logger

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_message(self):
        self.logger.info("This is a test log message.")
        with open(self.log_file, 'r') as file:
            logs = file.read()
            self.assertIn("This is a test log message.", logs)

    def test_log_json(self):
        data = {"key": "value"}
        self.logger.info("Logging JSON data.", extra={"data": data})
        with open(self.log_file, 'r') as file:
            logs = file.read()
            self.assertIn('"key": "value"', logs)

if __name__ == '__main__':
    unittest.main()
