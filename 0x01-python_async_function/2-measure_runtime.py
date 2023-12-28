#!/usr/bin/env python3
"""2-measure_runtime module"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures time to complet a task
    """
    start_time: float = time.time()
    for _ in range(n):
        asyncio.run(wait_n(1, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
