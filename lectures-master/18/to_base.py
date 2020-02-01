#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:48:33 2018

@author: jlopes

How to Think Like a Computer Scientist: Interactive Edition.
"""


def to_base(n, base):
    hexa = "0123456789ABCDEF"
    if n < base:
        return hexa[n]
    else:
        return to_base(n // base, base) + hexa[n % base]


print()
n = 2018
basis = [16, 10, 8, 2]
for b in basis:
    print(n, "to base", b, "-", to_base(n, b))
