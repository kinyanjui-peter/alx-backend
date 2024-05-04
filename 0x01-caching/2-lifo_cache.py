#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from BaseCaching.

This class implements a Last-In-First-Out (LIFO) caching system.

Attributes:
    cache_data (dict): Dictionary to store key-value pairs for caching.
"""

BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """LIFOCache class inherits from BaseCaching."""

    def __init__(self):
        """Initialize LIFOCache instance.

        Calls the __init__ method of the BaseCaching class.
        """
        super().__init__()

    def put(self, key, item):
        """Add a key-value pair to the cache.

        If the cache is full (reached the MAX_ITEMS limit) and the key is not already in the cache,
        remove the last item added to make space for the new item (LIFO algorithm).

        Args:
            key: Key of the item to be added.
            item: Value of the item to be added.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            # Cache is full, remove the last item added (LIFO)
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        # Add the new key-value pair to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value associated with the given key from the cache.

        Args:
            key: Key of the item to retrieve.

        Returns:
            Value associated with the key if found in the cache, None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]