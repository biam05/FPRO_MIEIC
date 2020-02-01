# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:59:11 2018

@author: biam05
"""

def local_minima(alist, n):
    notenumresult = [-3.4]
    result = []
    enumeratedlist = []
    for (index, value) in enumerate(alist):
        enumeratedlist.append((value, index))
    for i in range(len(alist)):
        if i < n//2 :
            sublist = alist[i:i+(n//2)+1]
        else:
            sublist = alist[i-(n//2):i+(n//2)+1]
        if alist[i] == min(sublist):
            if alist[i] not in notenumresult:
                result.append(enumeratedlist[i])
                notenumresult[0] = alist[i]
        else:
            notenumresult = [-3.4]
    return result         