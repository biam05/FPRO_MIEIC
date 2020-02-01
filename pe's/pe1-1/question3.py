# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:40:58 2019

@author: biam05
"""

names = ["bart", "marie", "jo"]
ages = [23, 75, 19]
final = ''

for i in range(len(names)):
    final += names[i] + '-' + str(ages[i]) + ' '
print(final[:len(final)-1])
