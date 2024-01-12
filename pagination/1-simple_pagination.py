#!/usr/bin/env python3
"""
method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function"""
    return ((page - 1) * page_size, page * page_size)


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
        """method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10."""
        assert type(page) is int and page >= 1
        assert type(page_size) is int and page_size >= 1
        pag = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pag[0]:pag[1]]
