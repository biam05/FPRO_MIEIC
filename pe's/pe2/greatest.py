# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:34:32 2019

@author: biam05
"""

def greatest(num):
    final = sorted(str(num), reverse = True)
    return int(''.join(final))