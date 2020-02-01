# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:18:04 2018

@author: biam05
"""

def sparse_dot_product(dict1, dict2):
    result = 0
    for i in dict1.keys():
        for j in dict2.keys():
            if i == j:
                result += dict1[i] * dict2[j]
            else:
                result += 0
    return result