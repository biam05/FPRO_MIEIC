# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:42:39 2018

@author: biam05
"""

def collisions(alist):
    count = {}
    hash_list = []
    for i in range(len(alist)):
        element = str(alist[i])
        x = 0
        for j in range(len(element)):
            x += int(element[j])
        hashs = x % 8
        hash_list.append(hashs)
    for hashs in hash_list:
        count[hashs] = count.get(hashs,0) +1             
    return count