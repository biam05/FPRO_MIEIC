# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:45:30 2018

@author: biam05
"""
def unique(atuple):
    result = ()
    atuple = sorted(atuple)
    for i in range (len(atuple)):
        if atuple[i] not in atuple[:i:]:
            result += (atuple[i],)
    return result