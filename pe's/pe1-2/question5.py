# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:23:25 2019

@author: biam05
"""

dec = int(input('Decimal number (base 10):'))
final = ''

while dec > 0:
    final += str(dec % 2)
    dec = dec // 2

print(final[::-1])