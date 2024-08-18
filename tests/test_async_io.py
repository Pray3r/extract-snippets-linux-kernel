import unittest
import asyncio
from src.utils.async_io import read_file_async

class TestAsyncIO(unittest.TestCase):
    def test_read_file_async(self):
        async def test():
            content = await read_file_async('test_file.txt')
            self.assertIsNotNone(content)
        asyncio.run(test())

if __name__ == '__main__':
    unittest.main()
