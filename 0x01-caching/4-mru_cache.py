#!/usr/bin/env python3
"""
Houses a child class MRUCache
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Implements a MRU caching system
    """

    def __init__(self):
        """
        Instantiates the class
        """
        super().__init__()
        self.items = []

    def put(self, key, item):
        """
        Maintains a MRU caching system in cache_data
        """
        if key and item:
            if key in self.items:
                self.items.remove(key)
            self.items.append(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least = self.items[-2]
            self.cache_data.pop(least)
            self.items.remove(least)
            print("DISCARD: {}".format(least))
        return

    def get(self, key):
        """
        Returns the value of the key from cache_data
        """
        if key and key in self.cache_data.keys():
            self.items.remove(key)
            self.items.append(key)
            return self.cache_data.get(key)
        return None
