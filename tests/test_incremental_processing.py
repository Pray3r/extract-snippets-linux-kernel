import unittest
import os
from src.processing.incremental_processing import IncrementalProcessor

class TestIncrementalProcessing(unittest.TestCase):
    def setUp(self):
        self.state_file = "test_state.txt"
        self.processor = IncrementalProcessor(state_file=self.state_file)
        self.files = ["file1.c", "file2.c"]

    def tearDown(self):
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

    def test_process_files_incrementally(self):
        def mock_process_function(file):
            return f"Processed {file}"

        self.processor.process_files(self.files, mock_process_function)
        processed_files = self.processor.processed_files
        self.assertEqual(processed_files, set(self.files))

        # Test that reprocessing skips already processed files
        new_files = ["file2.c", "file3.c"]
        self.processor.process_files(new_files, mock_process_function)
        self.assertEqual(self.processor.processed_files, set(self.files + ["file3.c"]))

if __name__ == '__main__':
    unittest.main()
