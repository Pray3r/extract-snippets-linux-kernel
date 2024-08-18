import unittest
from src.utils.mmap_utils import memory_map_file

class TestMmapUtils(unittest.TestCase):
    def test_memory_map_file(self):
        mm = memory_map_file('test_file.txt')
        self.assertIsInstance(mm, mmap.mmap)
        mm.close()

if __name__ == '__main__':
    unittest.main()
