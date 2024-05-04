#!/usr/bin/env python3
"""Create a class LFUCache that inherits from BaseCaching and is a caching system."""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFUCache class inherits from BaseCaching and implements a Least Frequently Used (LFU) caching system."""

    def __init__(self):
        """Initialize LFUCache instance."""
        super().__init__()
        self.frequencies = defaultdict(int)
        self.min_frequency = 0

    def update_frequency(self, key):
        """Update the frequency of the given key."""
        self.frequencies[key] += 1

    def evict(self):
        """Evict the least frequently used item (LFU algorithm) using LRU for tie-breaking."""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            min_frequency_keys = [key for key in keys if self.frequencies[key] == self.min_frequency]
            if min_frequency_keys:
                key_to_evict = min_frequency_keys[0]
                for key in min_frequency_keys:
                    if self.usedKeys.index(key) < self.usedKeys.index(key_to_evict):
                        key_to_evict = key
                del self.cache_data[key_to_evict]
                del self.frequencies[key_to_evict]
                self.usedKeys.remove(key_to_evict)
                print(f"DISCARD: {key_to_evict}")

    def put(self, key, item):
        """Add a key-value pair to the cache with LFU eviction strategy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.frequencies[key] = 0
            self.min_frequency = 0
            self.usedKeys.append(key)

    def get(self, key):
        """Retrieve the value associated with the given key from the cache."""
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        self.min_frequency = min(self.frequencies.values())
        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LFUCache()
