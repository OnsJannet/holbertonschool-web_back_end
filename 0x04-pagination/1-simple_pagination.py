#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    returns a tuple of size two containing a
    start index and an end index corresponding to
    the range of indexes to return in a list for
    those particular pagination parameters.
    '''

    size = page * page_size
    return (size - page_size, size)


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
        """get dataset
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        t1, t2 = index_range(page, page_size)
        pages = []
        if t1 >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[t1:t2]
