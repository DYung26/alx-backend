#!/usr/bin/env python3
"""
This module provides the MRUCache class, a caching system with a
Most Recently Used (MRU) eviction policy. MRUCache inherits from
BaseCaching and removes the most recently accessed item when the
cache exceeds its maximum capacity.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    Implements a Most Recently Used (MRU) caching policy, discarding
    the most recently accessed entry when the cache exceeds the MAX_ITEMS
    limit.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance and set up an OrderedDict
        for cache_data to track the order of item access.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache with the specified key. If adding
        the item causes the cache to exceed MAX_ITEMS, the most
        recently accessed entry is removed from the cache.

        Args:
            key: The key under which the item will be stored.
            item: The value to store in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Retrieve an item from the cache by key, marking it as
        recently accessed if it exists in the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The value associated with the specified key, or None
            if the key is not in the cache.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
