import asyncio

async def read_file_async(file_path):
    """Asynchronously read file contents."""
    loop = asyncio.get_event_loop()
    with open(file_path, 'r') as file:
        return await loop.run_in_executor(None, file.read)
