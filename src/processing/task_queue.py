from queue import Queue
from threading import Thread

class TaskQueue:
    def __init__(self):
        self.queue = Queue()
        self.results = []

    def add_task(self, task):
        self.queue.put(task)

    def run(self, worker_count=4):
        workers = []
        for _ in range(worker_count):
            worker = Thread(target=self.worker)
            worker.start()
            workers.append(worker)

        for worker in workers:
            worker.join()

    def worker(self):
        while not self.queue.empty():
            task = self.queue.get()
            result = task.run()
            self.results.append(result)
            self.queue.task_done()
