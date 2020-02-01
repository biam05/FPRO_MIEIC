# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:56:29 2019

@author: biam05
"""

def sum_pairs(alist):
    new_list= []
    for i in range(len(alist)-1):
        try:
            aux = alist[i] + alist[i+1]
            new_list.append(aux)            
        except TypeError:
            pass
    return new_list
    
print(sum_pairs([10, 3, 5, 'NA', 9, 1]))