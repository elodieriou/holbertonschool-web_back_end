#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary """
        assert 0 <= index < len(self.dataset())

        start: int = 0 if index is None else index
        end: int = page_size + start

        indexed_dataset: Dict[int, List] = self.indexed_dataset()
        data: List[List] = []

        for i in range(start, end):
            if i not in indexed_dataset:
                start += 1
                end += 1
        for i in range(start, end):
            data.append(indexed_dataset[i])

        next_index: int = end

        dictionary: Dict[str, Any] = {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }

        return dictionary
