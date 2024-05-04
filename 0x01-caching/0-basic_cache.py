#!/usr/bin/env python3
"""
Caching System
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize BasicCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add key-value pair to the cache

        Args:
            key: Key to be added
            item: Value to be associated with the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve value associated with the given key from cache

        Args:
            key: Key to retrieve the value for

        Returns:
            Value associated with the key if found, None otherwise
        """
        return self.cache_data.get(key, None)
