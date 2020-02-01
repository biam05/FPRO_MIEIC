# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:02:36 2018

@author: biam05
"""

def flatten(alist):
    final = []
    def flatten2(alist):
        for i in alist:
            if isinstance(i, str) or isinstance(i, int) or isinstance(i, float):
                final.append(i)
            else:
                flatten2(i)
        return final
    return flatten2(alist)


print(flatten(['Hello', [2, [[], False]], [True]]))