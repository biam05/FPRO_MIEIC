# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:23:50 2019

@author: biam05
"""

def treasure(clues):
    start = (0,0)
    while start in clues:
        old_start, start = start, clues[start]
        del clues[old_start]
    return start