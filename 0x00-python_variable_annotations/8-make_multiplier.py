#!/usr/bin/env python3
'''8-make_multiplier.py module'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    make_multiplier - creates a callable function
    args:
        multiplier - float variable
    return - multiplier_funtion
    '''

    def multiplier_function(x: float) -> float:
        '''
        multiplier_function - multiply two variable
        args:
            x - float variable
        return - x * multiplier
        '''

        return x * multiplier
    return multiplier_function
