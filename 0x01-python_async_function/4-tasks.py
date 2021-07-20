#!/usr/bin/env python3
''' a function that takes in an int argument named
that waits for a random delay between 0 and 10
seconds and eventually returns it.
'''
import random
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Prints a list of delays in ascending order. '''
    task = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(task)
