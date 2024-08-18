import os
import pickle

class CacheManager:
    def __init__(self, cache_dir='cache'):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    def save_to_cache(self, key, data):
        """Save data to cache with a specified key."""
        cache_file = os.path.join(self.cache_dir, f"{key}.pkl")
        with open(cache_file, 'wb') as file:
            pickle.dump(data, file)

    def load_from_cache(self, key):
        """Load data from cache using the specified key."""
        cache_file = os.path.join(self.cache_dir, f"{key}.pkl")
        if os.path.exists(cache_file):
            with open(cache_file, 'rb') as file:
                return pickle.load(file)
        return None
