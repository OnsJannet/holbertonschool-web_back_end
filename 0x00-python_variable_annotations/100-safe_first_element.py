#!/usr/bin/env python3
'''   returns values with the appropriate types
'''

from typing import Union, Sequence, Any, List


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''  return values with the appropriate types
    '''
    if lst:
        return lst[0]
    else:
        return None
