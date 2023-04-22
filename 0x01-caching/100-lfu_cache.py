#!/usr/bin/env python3
"""
Houses a child class LFUCache
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Implements a LFU caching system
    """
    def __init__(self):
        """
        Instantiates the class
        """
        super().__init__()
        self.track_freq = {}

    def put(self, key, item):
        """
        Maintain a LFU caching system in cache_data
        """
        # print("********************** {} *********************".format(key))

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.track_freq[key] += 1
                # print("====> {}".format(self.track_freq))
            else:
                first_in = sorted(self.track_freq.values())[0]
                # print("Checking for first in {}".format(self.track_freq))
                for k, value in self.track_freq.items():
                    if first_in == value:
                        first_in = k
                        break
                self.track_freq.pop(first_in)
            # first_in = list(self.cache_data)[0]
                self.cache_data.pop(first_in)
                print("DISCARD: {}".format(first_in))

        if ((key or item) and (key not in self.cache_data.keys())):
            self.cache_data[key] = item
            self.track_freq[key] = 0

    def get(self, key):
        """
        Returns the value of key in cache_data
        """
        if key and key in self.cache_data.keys():
            self.track_freq[key] += 1
            return self.cache_data.get(key)
        return None
