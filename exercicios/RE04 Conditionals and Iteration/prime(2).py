# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 08:35:26 2018

@author: biam05
"""

n = int(input("Integer: "))
divisor_list = []
for i in range (1, n+1):
    if (n % i) == 0:
        divisor_list.append(i)
    if len(divisor_list) == 2:
        result = True
    else:
        result = False

print(result)