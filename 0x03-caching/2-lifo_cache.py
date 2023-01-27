#!/usr/bin/python3
"""LIFOCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache implement method where the item that was added last
    is the first one to be removed when the cache reaches its maximum
    capacity.
    """

    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.list_of_keys = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.list_of_keys.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_update = self.list_of_keys[-2]
            self.cache_data.pop(last_update)
            print("DISCARD: {}".format(last_update))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
