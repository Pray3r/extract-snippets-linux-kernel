from concurrent.futures import ThreadPoolExecutor

class TaskScheduler:
    def __init__(self, max_workers=None):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def distribute_tasks(self, tasks, node_info):
        """Distribute tasks based on node load and network latency."""
        node_tasks = {node: [] for node in node_info}
        for task in tasks:
            best_node = min(node_info, key=lambda x: x['load'] + x['latency'])
            node_tasks[best_node['name']].append(task)
            best_node['load'] += 1  # Simulate load increase
        return node_tasks

    def execute_tasks(self, tasks):
        """Execute tasks using a thread pool."""
        future_to_task = {self.executor.submit(task): task for task in tasks}
        for future in future_to_task:
            try:
                result = future.result()
                print(f"Task {future_to_task[future]} completed with result: {result}")
            except Exception as exc:
                print(f"Task {future_to_task[future]} generated an exception: {exc}")
