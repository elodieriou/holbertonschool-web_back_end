#!/usr/bin/python3
"""FIFOCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache implement method where the item that was added first
    is the first one to be removed when the cache reaches its maximum
    capacity.

    This method is appropriate for situations where the rate of cache
    misses is not high and the data being cached is not frequently
    accessed again"""

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in = next(iter(self.cache_data))
            self.cache_data.pop(first_in)
            print("DISCARD: {}".format(first_in))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
