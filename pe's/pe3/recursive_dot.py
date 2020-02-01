# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:37:14 2019

@author: biam05
"""

def recursive_dot(l1, l2):
    if type(l1) == int:
        return l1 * l2
    if len(l1) == 0:
        return 0
    return recursive_dot(l1[0], l2[0]) + recursive_dot(l1[1:], l2[1:])