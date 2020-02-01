# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:40:04 2018

@author: biam05
"""

def sort_by_f(l):
    return sorted(l, key = lambda x: x if x < 5 else 5-x)