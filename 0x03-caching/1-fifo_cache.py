#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ BasicCache defines:
      - Inherits from BaseCaching
      - Cashing System with no limit
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary """
        if key is None or item is None:
            pass
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD: {}'.format(list(self.cache_data.keys())[0]))
            del self.cache_data[list(self.cache_data.keys())[0]]
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
