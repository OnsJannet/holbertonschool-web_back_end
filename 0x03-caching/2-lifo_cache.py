#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ BasicCache defines:
      - Inherits from BaseCaching
      - Cashing System with no limit
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ BaseCaching """
        self.discard = ""
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.discard)
            print('DISCARD:', self.discard)
        if key is not None:
            self.discard = key
        else:
            pass

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
