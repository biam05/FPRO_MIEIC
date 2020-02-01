# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:40:07 2019

@author: biam05
"""

def interleave(alist1, alist2):
    if type(alist1) != list:
        return [alist1, alist2]
    if len(alist1) == 0 or len(alist2) == 0:
        return []
    return interleave(alist1[0], alist2[0]) + interleave(alist1[1:], alist2[1:])