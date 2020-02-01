# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:44:03 2018

@author: biam05
"""

def override(l1, l2):
#    new_list = []
#    first_l2 = [l2[k][0] for k in range(len(l2))]
#    for i in range(len(l1)):
#        if l1[i][0] not in first_l2:
#            new_list.append(l1[i])
#    return sorted(l2 + new_list, key = lambda x: x[0])
    
    return sorted(l2 + [l1[i] for i in range(len(l1)) if l1[i][0] not in [l2[k][0] for k in range(len(l2))]], key = lambda x: x[0])