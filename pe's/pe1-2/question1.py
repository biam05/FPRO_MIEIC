# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:59:20 2019

@author: biam05
"""

ints = [1, 2, 2, 3, 5, 9, 13, 21, 34]
num = int(input('Number:'))
less = ''
greater = ''

for i in ints:
    if int(i) < num:
        less += str(i) + ' '
    elif int(i) > num:
        greater += str(i) + ' '

print('Less:', less[:len(less)-1])
print('Greater:', greater[:len(greater)-1])