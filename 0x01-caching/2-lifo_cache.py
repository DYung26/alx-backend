#!/usr/bin/env python3
"""
This module provides a LIFOCache class, a caching system with a
Last-In-First-Out (LIFO) eviction policy. LIFOCache inherits from
BaseCaching and removes the most recently added item when the cache
exceeds its max capacity.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching.
    Implements a Last-In-First-Out (LIFO) caching policy, discarding
    the most recently added entry when the cache exceeds the MAX_ITEMS limit.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance, setting up an
        OrderedDict for cache_data to maintain item order.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache with the specified key. If adding
        the item causes the cache to exceed MAX_ITEMS, the most
        recently added entry is removed from the cache.

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
                last_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

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
