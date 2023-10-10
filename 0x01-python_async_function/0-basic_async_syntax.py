#!/usr/bin/env python3
"""0-basic_async_syntax module"""


import asyncio
import random


async def wait_random(max_delay=10):
    """asyxhronous function"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
