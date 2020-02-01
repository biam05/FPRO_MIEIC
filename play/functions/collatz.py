# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:01:52 2019

@author: biam05
"""

def collatz(n):
    result = ''
    result += str(n)
    while n != 1:
        if n % 2 == 0:
            new = int(n / 2)
            n = new
            result +=',' + str(new)
        else:
            new = int(n * 3 + 1)
            n = new
            result +=',' + str(new)
    return result
        