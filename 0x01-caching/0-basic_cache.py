#!/usr/bin/env python3
"""
Houses the child class BasicCache
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a basic caching system
    """

    def put(self, key, item):
        """
        Adds items to the cache_data dictionary
        """
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value of a key in cache_data
        """
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
