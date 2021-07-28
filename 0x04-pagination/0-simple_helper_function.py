#!/usr/bin/env python3
'''
index_range
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    returns a tuple of size two containing a
    start index and an end index corresponding to
    the range of indexes to return in a list for
    those particular pagination parameters.
    '''

    size = page * page_size
    return (size - page_size, size)
