# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:49:24 2019

@author: biam05
"""

def solver(a, b, c):
    import math
    if (4 * a * c) > b**2:
        return []
    elif b**2 - 4*a*c == 0:
        return [-b/(2*a)]
    elif a == 0:
        return [(0-c)/b]
    else:
        x = (0-b + math.sqrt(b**2 - 4 * a * c))/(2*a)
        y = (0-b - math.sqrt(b**2 - 4 * a * c))/(2*a)
        if x == y:
            return [x]
        else:
            return sorted([x, y])