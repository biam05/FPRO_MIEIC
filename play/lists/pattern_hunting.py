# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:08:29 2019

@author: biam05
"""

def pattern_hunting(l1, l2, p):
    new_list = []
    for i in range(len(l1)):
        if p in l1[i]:
            new_list.append(l2[i])
        elif p in l2[i]:
            new_list.append(l1[i])
    return sorted(new_list, reverse = True)

l1=['a string', 'two strings', 'not here']
l2=['choose me', 'me too', 'but not me']
p='string'

print(pattern_hunting(l1, l2, p))