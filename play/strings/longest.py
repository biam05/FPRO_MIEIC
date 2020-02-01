# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:03:06 2019

@author: biam05
"""

def longest(s):
    lista = s.split(' ')
    return len(sorted(lista, key = len, reverse = True)[0])