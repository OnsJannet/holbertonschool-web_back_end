#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ BasicCache defines:
      - Inherits from BaseCaching
      - Cashing System with no limit
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ BaseCaching """
        self.cache = []
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            if key in self.cache_data:
                self.cache.remove(key)
            self.cache_data[key] = item
            self.cache.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.cache.pop(-2)
            del self.cache_data[discard]
            print('DISCARD:', discard)
        else:
            pass

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            self.cache.remove(key)
            self.cache.append(key)
            return self.cache_data[key]
