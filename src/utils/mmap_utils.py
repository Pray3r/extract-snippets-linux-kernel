import mmap

def memory_map_file(file_path):
    """Memory map a file for efficient reading."""
    with open(file_path, 'r+') as file:
        return mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
