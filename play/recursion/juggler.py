# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:43:45 2019

@author: biam05
"""

def juggler(n, p):
    import math
    if p == 0:
        return n
    if juggler(n, p-1) % 2 == 0:
        return math.floor((juggler(n,p-1))**0.5)
    elif juggler(n, p-1) % 2 != 0:
        return math.floor((juggler(n,p-1))**1.5)

print(juggler(3,2))