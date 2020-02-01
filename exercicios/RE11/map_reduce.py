# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:43:40 2018

@author: biam05
"""

def map_reduce(n1, n2):
    from functools import reduce
    
    lista_sqr = [i**2 for i in range(n1, n2) if i%2 != 0]
    return int(reduce(lambda x, y: x*y if x*y < 50 else x+y, lista_sqr))