#!/usr/bin/env python3
"""
A utility module for pagination support.

This module provides a function to calculate the start and end indices (range)
of items to retrieve from a dataset for a given page and page size.
"""
from typing import Tuple


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
