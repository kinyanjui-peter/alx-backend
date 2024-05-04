#!/usr/bin/env python3
""" This module defines a FIFO caching mechanism that inherits from BaseCaching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class inherits from BaseCaching.

    This caching strategy follows a First-In-First-Out (FIFO) policy.

    Attributes:
        cache_data (dict): Dictionary to store key-value pairs for caching.
    """

    def __init__(self):
        """Initialize FIFOCache instance.

        Calls the __init__ method of the BaseCaching class.
        """
        super().__init__()

    def put(self, key, item):
        """Add a key-value pair to the cache.

        If the cache is full (reached the MAX_ITEMS limit), remove the oldest item
        (the first item that was added) to make space for the new item.

        Args:
            key: Key of the item to be added.
            item: Value of the item to be added.
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                # Cache is full, remove the oldest item (first added)
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

            # Add the new key-value pair to the cache
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value associated with the given key from the cache.

        Args:
            key: Key of the item to retrieve.

        Returns:
            Value associated with the key if found in the cache, None otherwise.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)