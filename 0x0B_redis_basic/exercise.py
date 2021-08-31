#!/usr/bin/env python3
"""
exercise
"""

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, data: str, fn: Optional[Callable]) -> \
            Union[str, bytes, int, float]:
        ''' returns stored data '''
        fn_data = self._redis.get(data)
        if data:
            return fn(fn_data)
        else:
            return fn_data

    def get_str() -> str:
        ''' parametrize Cache.get with the correct
            conversion function
        '''
        return data.decode('utf-8')

    def get_int() -> int:
        ''' parametrize Cache.get with the correct
            conversion function
        '''
        return int(data)
