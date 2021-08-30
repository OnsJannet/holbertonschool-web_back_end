#!/usr/bin/env python3
"""
exercise
"""

import redis
import uuid
from typing import Union


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
