#!/usr/bin/env python3
"""0-basic_async_syntax module"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    asychronous function
    """

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
