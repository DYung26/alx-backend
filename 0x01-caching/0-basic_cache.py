#!/usr/bin/env python3
"""
This module defines the BasicCache class, a simple caching mechanism
that inherits from the BaseCaching class. The BasicCache class allows
storing and retrieving key-value pairs in memory without any limit or
eviction strategy.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    Provides a basic caching mechanism with no limit or eviction policy.
    """
    def __init__(self):
        """
        Initialize the BasicCache instance by calling the
        superclass's initializer to set up cache_data.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache with the specified key.

        Args:
            key: The key under which the item will be stored.
            item: The value to store in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
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
        if key is None:
            return None
        return self.cache_data.get(key, None)
