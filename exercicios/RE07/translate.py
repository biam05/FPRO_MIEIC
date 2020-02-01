# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:45:52 2018

@author: biam05
"""

def translate(astring, table):
    result = ''
    resultl = list(astring)
    for i in range (len(astring)):
        for j in range (len(table)):
            if table[j][0] == astring[i]:
                resultl[i] = str(table[j][1])
    result = ''.join(resultl)
    return result