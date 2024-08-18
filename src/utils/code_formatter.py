import subprocess

class CodeFormatter:
    @staticmethod
    def format_code_snippet(snippet, style='google'):
        """Format a code snippet according to the specified style."""
        try:
            formatted_code = subprocess.run(['clang-format', '--style', style],
                                            input=snippet.encode(),
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
            return formatted_code.stdout.decode()
        except subprocess.CalledProcessError as e:
            print(f"Error formatting code: {e}")
            return snippet
