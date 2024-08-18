import yaml

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from the YAML file."""
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def update_config(self, key, value):
        """Update a specific configuration setting."""
        self.config[key] = value
        with open(self.config_file, 'w') as file:
            yaml.safe_dump(self.config, file)
