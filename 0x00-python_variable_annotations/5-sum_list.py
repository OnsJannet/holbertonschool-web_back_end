#!/usr/bin/env python3
'''
takes a list input_list of floats
as argument and returns their sum as a float.

'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns the sum of a list of floats
    Args:
        input_list (float): [list of floats]
    Returns:
        float: [sum of list items]
    '''
    return sum(input_list)
