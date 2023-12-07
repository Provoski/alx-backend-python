#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
'''9-element_length.py module'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    element_length - goes through the length of list
    args:
        lst - list variable
    return - itema of lst
    '''
    return [(i, len(i)) for i in lst]
