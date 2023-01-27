#!/usr/bin/python3
"""LFUCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache implement method where the item that has been
    used least frequently is the first one to be removed"""

    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.update_order = []
        self.frequently_used = {}

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_list(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_frequently = self.findLFU()
            self.cache_data.pop(least_frequently)
            self.update_order.remove(least_frequently)
            self.frequently_used.pop(least_frequently)
            print("DISCARD: {}".format(least_frequently))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.update_order.remove(key)
            self.update_order.append(key)
            self.frequently_used[key] += 1
            return self.cache_data[key]
        return None

    def update_list(self, key):
        """Update the lists"""
        if key not in self.update_order and key not in self.frequently_used:
            self.update_order.append(key)
            self.frequently_used[key] = 1
        else:
            self.update_order.remove(key)
            self.update_order.append(key)
            self.frequently_used[key] += 1

    def findLFU(self):
        """Return the key least frequently used"""
        keys_least_frequently = []
        for i in self.frequently_used.items():
            if i[1] == 1:
                keys_least_frequently.append(i[0])

        if len(keys_least_frequently) > 1:
            return keys_least_frequently[0]
        else:
            return self.update_order[0]
