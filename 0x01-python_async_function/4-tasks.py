#!/usr/bin/env python3
"""4-tasks"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """module 2"""
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = await asyncio.gather(*tasks)

    # Append sorted results to delays
    delays.extend(sorted(results))

    return delays
