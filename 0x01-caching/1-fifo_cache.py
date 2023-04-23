#!/usr/bin/env python3
"""
Houses the child class FIFOCache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO caching system
    """
    def __init__(self):
        """
        Instantiates the class FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
        Maintains a FIFO caching system for cache_data
        """
        if key and item:
            self.cache_data[key] = item
        else:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in = list(self.cache_data)[0]
            self.cache_data.pop(first_in)
            print("DISCARD: {}".format(first_in))

    def get(self, key):
        """
        Returns the value of key in cache_data
        """
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
