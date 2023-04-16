#!/usr/bin/env python3
"""
Hypermedia pagination
"""


from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a Tuple of 2 integers; start index and end index corresponding
    to the range of indexes to return in a list of pagination parameters
    """
    end_index = page_size * page
    start_index = end_index - page_size
    # start_index = (page_size * page) - page_size
    return (start_index, end_index)


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
        Returns the appropriate page of the dataset correctly
        """
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)

        try:
            indexes = index_range(page, page_size)
            start, end = [index for index in indexes]
            data = self.dataset()
            paged_data = []
            for content in range(start, end):
                paged_data.append(data[content])
        except IndexError:
            paged_data = []
        return paged_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing; page_size, page, data,
        next_page, prev_page, and total_pages
        """
        page_content = self.get_page(page, page_size)
        data = self.dataset()
        total_pages = ((len(data) - 1) // page_size) + 1
        return {
                "page_size": len(page_content),
                "page": page,
                "data": page_content,
                "next_page": None if page >= total_pages else page + 1,
                "prev_page": None if page - 1 == 0 else page - 1,
                "total_pages": total_pages
                }
