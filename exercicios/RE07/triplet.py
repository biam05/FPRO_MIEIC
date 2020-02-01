# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:21:47 2018

@author: biam05
"""

def triplet(atuple):
    result = ()
    for i in range (len(atuple)-1):
        for j in range (i+1, len(atuple)):
            for k in range (j+1, len(atuple)):
                if (int(atuple[i]) + int(atuple[j]) + int(atuple[k])) == 0:
                    result += (atuple[i], atuple[j], atuple[k],)
                    if result[:3] > result[4:]:
                        result = result[:3]
                    else:
                        result = result[4:]
    return result