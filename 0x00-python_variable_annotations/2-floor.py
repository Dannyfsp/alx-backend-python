#!/usr/bin/env python3
'''
Description:    takes a float as arg and returns a floor
Argument:       n: float
'''


def floor(n: float) -> int:
    '''Return largest int value less than or equal to n'''
    return int(n) if n >= 0 else int(n) - 1
