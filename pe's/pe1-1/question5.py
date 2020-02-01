# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:52:38 2019

@author: biam05
"""

dec = int(input('Decimal number (base 10):'))

result = ''

while dec > 0:
    result += str(dec%8)
    dec = dec//8

print(result[::-1])
    
    