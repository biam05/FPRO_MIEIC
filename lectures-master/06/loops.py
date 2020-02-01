#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:15:42 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

###### generate ten million random numbers

import time

import random
rnd = random.Random()

## Version 1
## Build a list of random numbers, then sum them

start_time = time.time()
numbers = []
print("doing it...")
for _ in range(100000000):
    num = rnd.randrange(1000)  # Generate one random number
    numbers.append(num)        # Save it in our list

tot = sum(numbers)
print(tot)
print("--- %s seconds" % (time.time() - start_time))

## Version 2
## Sum the random numbers as we generate them

#start_time = time.time()
#print("doing it...")
#tot = 0
#for _ in range(100000000):
#    num = rnd.randrange(1000)
#    tot += num
#print(tot)
#print("--- %s seconds" % (time.time() - start_time))
