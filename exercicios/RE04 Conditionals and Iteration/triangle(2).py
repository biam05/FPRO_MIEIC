# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:42:58 2018

@author: biam05
"""

n1 = int(input("Size 1: "))
n2 = int(input("Size 2: "))
n3 = int(input("Size 3: "))

if n1 <= (n2 + n3) or n2 <= (n1 + n3) or n3 <= (n1 + n2) or n1 < 0 or n2 < 0 or n3 < 0:
    result = str("Not a triangle")
else:
    if n1 == n2 and n2 == n3:
        result = str("Equilateral")
    else:
        if n1 == n2 or n2 == n3 or n1 == n3:
            result = str("Isosceles")
        else:
            result = str("Scalene")

print(result)

