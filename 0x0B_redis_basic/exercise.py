#!/usr/bin/env python3
"""
exercise
"""

import redis
import uuid
from typing import Union, Callable, Optional


def count_calls(methode: Callable) -> Callable:
    ''' counts the times a function is 
        being called
    '''
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper '''
        self._redis.incr(key)
        return method(self, rgs, **kwargs)
    return wrapper


class Cache:
    ''' Cache '''
    def __init__(self):
        ''' Init '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Stores a key '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, data: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        ''' returns stored data '''
        if data:
            fn_data = self._redis.get(data)
            if fn:
                return fn(fn_data)
            else:
                return fn_data

    def get_str(self, data: bytes) -> str:
        ''' parametrize Cache.get with the correct
            conversion function
        '''
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        ''' parametrize Cache.get with the correct
            conversion function
        '''
        return int(data)
