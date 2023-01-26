#!/usr/bin/python3
"""LIFOCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache implement method where the item that was added last
    is the first one to be removed when the cache reaches its maximum
    capacity.
    """

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = [item]

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            rev = reversed(self.cache_data)
            last_in = next(rev) and next(rev)
            self.cache_data.pop(last_in)
            print("DISCARD: {}".format(last_in))

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
