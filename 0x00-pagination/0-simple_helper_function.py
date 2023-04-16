#!/usr/bin/env python3
"""
Helper function for pagination indexing
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a Tuple of 2 integers; start index and end index corresponding
    to the range of indexes to return in a list of pagination parameters
    """
    end_index = page_size * page
    start_index = end_index - page_size
    # start_index = (page_size * page) - page_size
    return (start_index, end_index)
