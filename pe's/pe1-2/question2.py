# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:04:09 2019

@author: biam05
"""

number = int(input('Non Negative Number:'))
count = 0

while number > 10:
    if (number % 100) // 10 == number % 10:
        count += 1
    number = number // 10

print(count)