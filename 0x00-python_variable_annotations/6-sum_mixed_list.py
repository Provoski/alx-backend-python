#!/usr/bin/python3
'''6-sum_mixed_list.py module'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sum_mixed_list - calculate thw sum ofixed list of int and float
    args:
        mxd_lst - variable for list of mixed type
    return - sum of mxd_lst
    '''

    return float(sum(mxd_lst))
