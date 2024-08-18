import unittest
import os
from src.utils.file_utils import FileUtils

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.txt"
        self.content = "This is a test file."

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_write_file(self):
        FileUtils.write_file(self.test_file, self.content)
        read_content = FileUtils.read_file(self.test_file)
        self.assertEqual(self.content, read_content)

    def test_list_files(self):
        FileUtils.write_file(self.test_file, self.content)
        files = FileUtils.list_files('.', '.txt')
        self.assertIn(self.test_file, files)

if __name__ == '__main__':
    unittest.main()
