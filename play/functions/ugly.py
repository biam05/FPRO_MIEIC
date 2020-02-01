# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:47:53 2019

@author: biam05
"""

def ugly(n):
    if n == 0:
        return False
    for i in [2, 3, 5]:
        while n % i == 0:
            n = n / i
    if n == 1:
        return True
    return False