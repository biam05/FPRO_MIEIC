# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:58:50 2019

@author: biam05
"""

def discard_middle(s):
    if len(s) <= 3:
        return ''
    else:
        return s[:2] + s[-2:]