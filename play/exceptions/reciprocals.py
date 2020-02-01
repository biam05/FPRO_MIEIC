# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:48:45 2019

@author: biam05
"""

def reciprocals(alist):
    new_list = []
    for n in alist:
        try:
            new_list.append(1/n)
        except TypeError:
            pass
        except ZeroDivisionError:
            pass
    return new_list