# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:13:54 2018

@author: biam05
"""

def roman_to_integer(astring):
    total = 0
    integer = []
    converter = {}
    converter['I'] = 1
    converter['V'] = 5
    converter['X'] = 10
    converter['L'] = 50
    converter['C'] = 100
    converter['D'] = 500
    converter['M'] = 1000
    for i in astring:
        integer.append(str(converter[i])) 
    for j in range(len(integer)-1):
        if int(integer[j]) >= int(integer[j+1]):
            total += int(integer[j])
        else:
            total = total - int(integer[j])
    if integer[len(integer)-1] >= integer[len(integer)-2]:
        total += int(integer[len(integer)-1])
    else:
        total = total - int(integer[len(integer)-1])
    return total

print(roman_to_integer('MMMCMXCIX'))