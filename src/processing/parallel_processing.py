from multiprocessing import Pool

class ParallelProcessor:
    def __init__(self, max_workers=None):
        self.pool = Pool(processes=max_workers)

    def run_tasks(self, tasks):
        """Run tasks in parallel using multiprocessing."""
        results = self.pool.map(self._execute_task, tasks)
        return results

    def _execute_task(self, task):
        """Helper function to execute a task."""
        return task.run()
