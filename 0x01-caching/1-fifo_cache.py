#!/usr/bin/env python3
"""
This module defines the FIFOCache class, a caching mechanism with a
First-In-First-Out (FIFO) eviction policy. The FIFOCache inherits from
BaseCaching and removes the oldest item when the cache reaches its max limit.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.
    Implements a First-In-First-Out (FIFO) caching policy, discarding
    the oldest entry when the cache exceeds the MAX_ITEMS limit.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance by calling the
        superclass's initializer to set up cache_data.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache with the specified key. If adding
        the item causes the cache to exceed MAX_ITEMS, the oldest
        entry is removed from the cache.

        Args:
            key: The key under which the item will be stored.
            item: The value to store in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The value associated with the specified key, or None
            if the key is not in the cache.
        """
        return self.cache_data.get(key, None)
