#!/usr/bin/env python3
"""
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.track_freq = {}

    def put(self, key, item):
        """
        """
        # print(sorted(self.track_freq.values()))
        '''
        if key in self.cache_data.keys():
            d_key = key
            self.cache_data[key] = item
            print("Put")
            self.track_freq[key] += 1
            print("====> {}".format(self.track_freq))
        '''
        # elif key or item and key not in self.cache_data.keys():
            # self.cache_data[key] = item
            # self.track_freq[key] = 0A
        print("************************* {} ************************".format(key))

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            # print("key ", key)
            if key in self.cache_data.keys():
                print("Put")
                self.cache_data[key] = item
                self.track_freq[key] += 1
                print(self.cache_data)
                print("====> {}".format(self.track_freq))
                r = key in self.cache_data.keys()
                print(r)
            else:
                print('Here2')
                first_in = sorted(self.track_freq.values())[0]
                print("Checking for first in {}".format(self.track_freq))
                for k, value in self.track_freq.items():
                    if first_in == value:
                        first_in = k
                        break
            # print(first_in)
                self.track_freq.pop(first_in)
                print(self.track_freq)
            # first_in = list(self.cache_data)[0]
                self.cache_data.pop(first_in)
                print("DISCARD: {}".format(first_in))

        if ((key or item) and (key not in self.cache_data.keys())):
            print('Here1')
            print(self.track_freq)
            self.cache_data[key] = item
            self.track_freq[key] = 0
            print(self.cache_data)
            print(self.track_freq)

    def get(self, key):
        """
        """
        print(self.track_freq)
        if key and key in self.cache_data.keys():
            self.track_freq[key] += 1
            # print("Gotten {}".format(key))
            return self.cache_data.get(key)
        return None

