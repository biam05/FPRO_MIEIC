# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:11:46 2019

@author: biam05
"""

def count_exceptions(f, n1, n2):
    count = 0
    for number in range(n1, n2+1):
        try:
            f(number)
        except:
            count += 1
    return count
    