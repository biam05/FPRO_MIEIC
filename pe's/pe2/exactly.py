# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:37:15 2019

@author: biam05
"""

def exactly(s):
    tup = ()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i].isdigit() and s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
                substring = s[i+1:j]
                if substring.count('?') == 3:
                    tup += (s[i] + s[j],)
                else:
                    tup = (s[i] + s[j],)
                    return 'The sequence {0} is NOT OK with first violation with pair: {1}'.format(s, tup)
    return 'The sequence {0} is OK with the pairs: {1}'.format(s, tup)

print(exactly("b8i???2rjub5???B?u7??gkroi3???7kg?9"))                    