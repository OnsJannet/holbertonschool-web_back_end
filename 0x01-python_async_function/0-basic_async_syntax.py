#!/usr/bin/env python3
''' a function that takes in an int argument named
that waits for a random delay between 0 and 10
seconds and eventually returns it.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' waits between 0 and 10 tp return an int '''

    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
