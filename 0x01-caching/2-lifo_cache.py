#!/usr/bin/env python3
"""
Houses the child class LIFOCache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements a LIFO Caching system
    """

    def __init__(self):
        """
        Instantiates the class
        """
        super().__init__()

    def put(self, key, item):
        """
        Maintains a LIFO caching system for cache_data
        """
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                last_in = key
            else:
                last_in = list(self.cache_data)[-1]
                print("DISCARD: {}".format(last_in))
            self.cache_data.pop(last_in)
        if key or item:
            self.cache_data[key] = item
        return

    def get(self, key):
        """
        Returns the value of key in cache_data
        """
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
