#!/usr/bin/env python3
"""Create a class LRUCache that inherits from BaseCaching.

This class implements a Least Recently Used (LRU) caching system.

Attributes:
    cache_data (dict): Dictionary to store key-value pairs for caching.
    usedKeys (list): List to track the order of key usage (most recent keys are at the end).
"""

BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """LRUCache class inherits from BaseCaching."""

    def __init__(self):
        """Initialize LRUCache instance.

        Calls the __init__ method of the BaseCaching class and initializes usedKeys list.
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """Add a key-value pair to the cache.

        If the cache is full (reached the MAX_ITEMS limit), remove the least recently used item
        to make space for the new item (LRU algorithm).

        Args:
            key: Key of the item to be added.
            item: Value of the item to be added.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key in self.usedKeys:
            # Move the key to the end of the usedKeys list (recently used)
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
        else:
            # Add the key to the end of the usedKeys list (newly added)
            self.usedKeys.append(key)

        if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
            # Cache is full, remove the least recently used item (LRU)
            discard = self.usedKeys.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Retrieve the value associated with the given key from the cache.

        If the key exists in the cache, move
        it to the end of the usedKeys list (recently used).

        Args:
            key: Key of the item to retrieve.

        Returns:
            Value associated with the key if found in the cache, None otherwise.
        """
        if key is not None and key in self.cache_data:
            # Move the key to the end of the usedKeys list (recently used)
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data[key]
        return None
