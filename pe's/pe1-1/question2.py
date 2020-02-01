# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:37:31 2019

@author: biam05
"""

d = input('Integer with 1 digit:')
num = input('Another number:')
result = 0

for i in list(num):
    if int(i) > int(d):
        result += 2 * int(i)

print(result)