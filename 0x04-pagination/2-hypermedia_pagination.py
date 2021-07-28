#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List, Tuple, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        '''returns a dictionary where
        page_size: the length of thereturned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer

        '''
        data = self.get_page(page, page_size)
        total_pages = math.floor(len(self.dataset()) / page_size)
        page_sizes = len(self.get_page(page, page_size))
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page > 1 else None
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        return {'page_size': page_sizes, 'page': page, 'data': data,
                'next_page': next_page, 'prev_page': prev_page,
                'total_pages': total_pages}
