# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:12:31 2018

@author: biam05
"""

n = int(input("n = "))

nn = str(n) + str(n)
nnn = str(n) + str(n) + str(n)

expression = n + int(nn) + int(nnn)

print("n + nn + nnn =", expression)