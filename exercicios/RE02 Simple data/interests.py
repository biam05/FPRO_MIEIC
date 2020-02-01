# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:15:42 2018

@author: biam05
"""

p = int(input("Principal amount:"))
n = int(input("The frequency that the interest is paid out (per year):"))
r = float(input("The interest rate:"))
t = 2

a = p * ( 1 + (r/n))**(n*t)

print("Final amount if one is earning compound interest:", a)

