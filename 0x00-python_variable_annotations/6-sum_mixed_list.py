#!/usr/bin/env python3
'''
takes a list mxd_lst of integers
and floats and returns their sum as a float.

'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns the sum of a list of floats and intergers
    Args:
        mxd_lst (float, int): [list of floats & integers]
    Returns:
        float: [sum of list items]
    '''
    return sum(mxd_lst)
