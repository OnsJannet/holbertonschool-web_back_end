#!/usr/bin/env python3
''' takes an integer max_delay and returns a asyncio.Task
'''
import asyncio
import random
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:

    ''' returns task'''
    return asyncio.create_task(wait_random(max_delay))
