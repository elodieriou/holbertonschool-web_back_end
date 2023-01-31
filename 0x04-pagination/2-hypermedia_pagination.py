#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


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
        """Return the data at the appropriate page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexes = index_range(page, page_size)
        start = indexes[0]
        end = indexes[1]
        data = self.dataset()

        return [] if start >= len(data) else data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary with the following values:
        - page_size: number elements in the page
        - page: number of the current page
        - data: data between [star:end]
        - next_page: number of the next page
        - prev_page: number of the prev page
        - total_page: total number of pages
        And calculate indexes to know the start and end.
        Careful to calculate the data at first, before change the values of
        page and page_size"""

        data = self.get_page(page, page_size)
        indexes = index_range(page, page_size)
        dataset_size = len(self.dataset())

        dictionary = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if indexes[1] < dataset_size else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_page': math.ceil(dataset_size / page_size)
        }

        return dictionary
