#!/usr/bin/env python3
"""
A utility module for pagination support.

This module provides a function to calculate the start and end indices (range)
of items to retrieve from a dataset for a given page and page size.
"""
from typing import Tuple
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the range of item indices for pagination.

    Args:
        page (int): The page number (1-based).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (offset) and
                         the end index (limit) for the specified page.
    """
    offset = (page - 1) * page_size
    limit = offset + page_size
    return (offset, limit)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of items from the dataset.

        Args:
            page (int): The page number (1-based, must be > 0).
            page_size (int): The number of items per page (must be > 0).

        Returns:
            List[List]: The items for the specified page, or an empty list
                        if the page is out of range.

        Raises:
            AssertionError: If page or page_size is not a positive integer.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)
        return dataset[start_idx:end_idx] if start_idx < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        return {
            'page_size': page_size, 'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page+1 if self.get_page(page+1, page_size) else None,
            'prev_page': page-1 if page-1 != 0 else None,
            'total_pages': math.ceil(len(self.dataset())/page_size)
        }
