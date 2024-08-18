import unittest
from src.processing.task_queue import TaskQueue
from src.processing.chunk_processing import ChunkProcessor

class MockTask:
    def __init__(self, value):
        self.value = value

    def run(self):
        return self.value * 2

class TestProcessing(unittest.TestCase):
    def test_task_queue(self):
        queue = TaskQueue()
        queue.add_task(MockTask(5))
        queue.add_task(MockTask(10))
        queue.run(worker_count=2)
        self.assertEqual(queue.results, [10, 20])

    def test_chunk_processing(self):
        processor = ChunkProcessor(chunk_size=2)
        data = [1, 2, 3, 4, 5]
        result = processor.process_in_chunks(data, lambda chunk: [x * 2 for x in chunk])
        self.assertEqual(result, [[2, 4], [6, 8], [10]])

if __name__ == '__main__':
    unittest.main()
