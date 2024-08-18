class ChunkProcessor:
    def __init__(self, chunk_size):
        self.chunk_size = chunk_size

    def process_in_chunks(self, data, process_function):
        """Process data in chunks using the provided processing function."""
        results = []
        for i in range(0, len(data), self.chunk_size):
            chunk = data[i:i + self.chunk_size]
            result = process_function(chunk)
            results.append(result)
        return results
