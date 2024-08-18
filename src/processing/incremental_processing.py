import os

class IncrementalProcessor:
    def __init__(self, state_file='processing_state.txt'):
        self.state_file = state_file
        self.processed_files = self._load_state()

    def _load_state(self):
        """Load the list of already processed files from a state file."""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as file:
                return set(file.read().splitlines())
        return set()

    def _save_state(self):
        """Save the list of processed files to the state file."""
        with open(self.state_file, 'w') as file:
            for filename in self.processed_files:
                file.write(filename + '\n')

    def process_files(self, files, process_function):
        """Process files incrementally, skipping already processed files."""
        for file in files:
            if file not in self.processed_files:
                process_function(file)
                self.processed_files.add(file)
                self._save_state()
