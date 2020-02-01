# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:01:07 2018

@author: biam05
"""

def odd_range(start, stop, step):
    odds = list(i for i in range(start, stop) if i%2!=0)
    for i in range(len(odds)):
        if i % step == 0:
            yield odds[i]