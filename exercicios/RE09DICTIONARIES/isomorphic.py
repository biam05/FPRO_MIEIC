# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:47:40 2018

@author: biam05
"""

def isomorphic(astring1, astring2):
    converter = {}
    news2 = ''
    for i in range(len(astring2)):
        converter[astring1[i]] = astring2[i]
    for i in range(len(astring2)):
        news2 += converter[astring1[i]]
    alist = []
    valuelist = []
    for key, value in converter.items():
        alist.append((key, value))
        if value not in valuelist:
            valuelist.append(value)
    if news2 == astring2 and len(alist) == len(valuelist):
        return '\'{0}\' and \'{1}\' are isomorphic because we can map: {2}'.format(astring1,astring2,alist)
    else:
        return '\'{0}\' and \'{1}\' are not isomorphic'.format(astring1, astring2)
print(isomorphic('turtle', 'tletur'))    