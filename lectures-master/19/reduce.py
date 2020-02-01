#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:04:18 2018

@author: jlopes
"""

def plus(a, b):
    return a+b

def oddn(n):
    return 2*n+1

print()
for i in range(10):
    # sq = reduce(plus, map(oddn, range(i)), 0)
    sq = 0
    for s in map(oddn, range(i)):
        sq = plus(sq, s)
    print(i, sq)
