#!/usr/bin/python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) >= (self.MAX_ITEMS):
            firstKey = next(iter(self.cache_data))
            del self.cache_data[firstKey] 
            print("DISCARD: {}", firstKey)
        # raise NotImplementedError("put must be implemented in your
        # cache class")

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key not in self.cache_data:
            return None
        return self.cache_data[key]

        # raise NotImplementedError("get must be implemented in your
        # cache class")
