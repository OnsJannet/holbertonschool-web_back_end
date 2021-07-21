#!/usr/bin/env python3
''' Description: coroutine will collect 10 random
numbers using an async comprehensing over
async_generator, then return the 10 random numbers
'''
import random
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
        Collect 10 numbers and return them

    '''
    numbers = []
    async for number in async_generator():
        numbers.append(number)
    return(numbers)
