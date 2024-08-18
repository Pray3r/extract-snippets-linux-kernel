import unittest
from src.utils.async_io import read_file_async
from src.utils.mmap_utils import memory_map_file

class TestUtils(unittest.TestCase):
    def test_read_file_async(self):
        content = "This is a test."
        with open('test_async.txt', 'w') as f:
            f.write(content)
        
        async def run_test():
            read_content = await read_file_async('test_async.txt')
            self.assertEqual(read_content, content)

        import asyncio
        asyncio.run(run_test())
        os.remove('test_async.txt')

    def test_memory_map_file(self):
        content = "This is a test."
        with open('test_mmap.txt', 'w') as f:
            f.write(content)
        
        mm = memory_map_file('test_mmap.txt')
        self.assertEqual(mm[:].decode('utf-8'), content)
        mm.close()
        os.remove('test_mmap.txt')

if __name__ == '__main__':
    unittest.main()
