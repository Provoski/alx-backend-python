#!/usr/bin/python3
'''9-element_length.py module'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    element_length - goes through the length of list
    args:
        lst - list variable
    return - itema of lst
    '''
    return [(i, len(i)) for i in lst]
