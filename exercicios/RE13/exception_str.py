# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:04:01 2019

@author: biam05
"""

def exception_str(f):
    try:
        f()
        return 'No exception was raised'
    except Exception as ex:
        return str(ex)