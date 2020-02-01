# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:13:16 2019

@author: biam05
"""

integers = [0, 2, 9, 15, 64]
reals = [0.0, 3.2, 8.4, 15.5,128.0]
final = ''

for i in range(len(integers)):
    final += str(max(integers[i], reals[i])) + ' '

print(final[:len(final)-1])
