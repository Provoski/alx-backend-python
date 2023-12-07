#!/usr/bin/python3
'''7-to_kv.py module'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    to_kv - convert variable to tubles element
    args:
        k - string variable
        v - int or float variable
    return - tuple of k and square of v
    '''

    return k, float(v**2)
