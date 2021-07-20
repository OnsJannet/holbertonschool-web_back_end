#!/usr/bin/env python3
''' measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
'''
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:

    ''' returns the elapsed time'''
    start_task = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_task = time.time()
    total_time: float = end_task - start_task
    return total_time / n
