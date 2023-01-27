#!/usr/bin/python3
"""LRUCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache implement method where the item that has been
    used least recently is the first one to be removed"""

    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.list_of_keys = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_list(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recently = self.list_of_keys[0]
            self.cache_data.pop(least_recently)
            self.list_of_keys.remove(least_recently)
            print("DISCARD: {}".format(least_recently))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.list_of_keys.remove(key)
            self.list_of_keys.append(key)
            return self.cache_data[key]
        return None

    def update_list(self, key):
        """Update a list"""
        if key not in self.list_of_keys:
            self.list_of_keys.append(key)
        else:
            self.list_of_keys.remove(key)
            self.list_of_keys.append(key)
