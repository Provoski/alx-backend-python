#!/usr/bin/env python3
import asyncio
import random
from typing import List
"""1-concurrent_coroutines module"""


if __name__ == "__main__":
    async def wait_random(max_delay: float = 10) -> float:
        """module 1"""
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        return delay

    async def wait_n(n: int, max_delay: float) -> List[float]:
        """module 2"""
        delays: List[float] = []
        tasks = [wait_random(max_delay) for _ in range(n)]
        results = await asyncio.gather(*tasks)
        delays = sorted(results)
        return delays 
