# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:17:29 2019

@author: biam05
"""

def compatible(A, B):
    try:
        assert len(A[0]) == len(B), 'A and B cannot be multiplied'
    except AssertionError as erro:
        return erro
    return 'A and B can be multiplied' 