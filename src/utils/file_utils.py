import os

class FileUtils:
    @staticmethod
    def read_file(file_path):
        """Read a file and return its contents."""
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        """Write content to a file."""
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def list_files(directory, extension=None):
        """List all files in a directory with an optional extension filter."""
        return [os.path.join(directory, f) for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f)) and (extension is None or f.endswith(extension))]
