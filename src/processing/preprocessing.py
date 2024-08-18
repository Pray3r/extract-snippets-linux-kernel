import subprocess

class Preprocessor:
    def preprocess_code(self, source_code):
        """Preprocess the source code to handle macros and conditional compilation."""
        try:
            preprocessed_code = subprocess.check_output(
                ['gcc', '-E', '-'], input=source_code.encode(), stderr=subprocess.PIPE
            )
            return preprocessed_code.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Preprocessing failed: {e}")
            return source_code
