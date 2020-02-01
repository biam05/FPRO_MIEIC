# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:45:29 2019

@author: biam05
"""

def dogs(h_age):
    if h_age <= 2:
        return h_age * 10.5
    else:
        return 2 * 10.5 + (h_age - 2) * 4
