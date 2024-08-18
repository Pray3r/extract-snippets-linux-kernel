class BatchProcessor:
    def __init__(self, batch_size):
        self.batch_size = batch_size

    def process_in_batches(self, tasks, process_function):
        """Process tasks in batches using the provided processing function."""
        results = []
        for i in range(0, len(tasks), self.batch_size):
            batch = tasks[i:i + self.batch_size]
            result = process_function(batch)
            results.append(result)
        return results
