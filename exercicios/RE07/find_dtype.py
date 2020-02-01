# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:08:41 2018

@author: biam05
"""

def find_dtype(atuple, data_type):
    result = ()
    for i in range (0, len(atuple)):
        a_tuple = type(atuple[i]).__name__
        if data_type == a_tuple:
            result += (atuple[i],)
    return result

