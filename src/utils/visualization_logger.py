import json

class VisualizationLogger:
    def __init__(self, log_file='visual_log.json'):
        self.log_file = log_file
        self.logs = []

    def log_event(self, event_type, data):
        """Log an event with its type and associated data."""
        self.logs.append({"type": event_type, "data": data})
        self._write_to_file()

    def _write_to_file(self):
        """Write the logs to a file."""
        with open(self.log_file, 'w') as file:
            json.dump(self.logs, file, indent=4)
