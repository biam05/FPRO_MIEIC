# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:50:03 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


# This is a particularly inefficient algorithm, and this could be solved
# far more efficient iteratively or using memoisation
def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


import time

t0 = time.clock()
n = 42   # 35
result = fib(n)
t1 = time.clock()
print()
print("Computing...", end="", flush=True)
print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

