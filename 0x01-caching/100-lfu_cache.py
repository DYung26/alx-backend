#!/usr/bin/env python3
"""
Least Frequently Used (LFU) caching module.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    Implements a Least Frequently Used (LFU) caching policy, discarding
    the least frequently used entry when the cache exceeds the MAX_ITEMS limit.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance with cache data and frequency
        tracking.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []  # Stores [key, frequency] pairs in insertion order

    def __reorder_items(self, mru_key):
        """
        Reorder the items in cache based on access frequency.
        Increments the frequency of the given key and repositions it in
        the frequency list.

        Args:
            mru_key: The key to update and reorder in the frequency list.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0

        for i, (key, freq) in enumerate(self.keys_freq):
            if key == mru_key:
                mru_freq = freq + 1
                mru_pos = i
                break
            if not max_positions or freq < \
                    self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)

        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos

        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """
        Add an item to the cache with the specified key. If adding the item
        causes the cache to exceed MAX_ITEMS, the least frequently used item
        is removed from the cache.

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
                lfu_key, _ = self.keys_freq.pop()
                self.cache_data.pop(lfu_key)
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = next((i for i, (_, freq) in enumerate(self.keys_freq)
                              if freq == 0), len(self.keys_freq))
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key, marking it as accessed.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The value associated with the specified key, or None if the key
            is not in the cache.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
