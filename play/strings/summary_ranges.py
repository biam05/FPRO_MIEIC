# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:18:01 2019

@author: biam05
"""

def summary_ranges(astring):
    new_list = []
    aux = []
    alist = astring.split(',')
    for i in range(len(alist)):
        if i != len(alist)-1:
            if int(alist[i]) + 1 == int(alist[i+1]):
                aux.append(alist[i])
                aux.append(alist[i+1])
            else:
                if len(aux) > 1:
                    new_list.append('{0}->{1}'.format(aux[0], aux[-1]))
                    aux = []
                else:
                    new_list.append(alist[i])
        else:
            if int(alist[i]) - 1 == int(alist[i-1]):
                aux.append(alist[i-1])
                aux.append(alist[i])

#            if len(aux) > 1:
                new_list.append('{0}->{1}'.format(aux[0], aux[-1]))
                aux = []
            else:
                new_list.append(alist[i])
    return ','.join(new_list)
            

print(summary_ranges("0,1,2,3,4,5,7,10,11,20,21"))