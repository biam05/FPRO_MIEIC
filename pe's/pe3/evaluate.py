# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:35:30 2019

@author: biam05
"""

def evaluate(a, x):
    return sum(ai*x**e for e, ai in enumerate(a))