# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:52:15 2018

@author: biam05
"""
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
x = n1
y = n2
i = 0
result = 0
while y > 0:
    y = y % 10
    result += (y*(10**(i)))
    y = n2 - result
    y = y / (10**(i))
    i += 1
while x > 0:
    x = x % 10
    result += (x*(10**(i)))
    x = (n1*(10**i)) - result
    x = x / (10**i)
    i += 1
print(result)