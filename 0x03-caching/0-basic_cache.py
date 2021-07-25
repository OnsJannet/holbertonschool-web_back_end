#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Inherits from BaseCaching
      - Cashing System with no limit
      - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """ Assign to the dictionary """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
