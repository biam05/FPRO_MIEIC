#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:42:43 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

###### does the list have any odd numbers?

numbers = [10, 5, 24, 8, 6]

## 1. Buggy version

#for number in numbers:
#    if number % 2 == 1:
#        print(True)
#        break
#    else:
#        print(False)
#        break

## 2. for ... else construct?!

#for number in numbers:
#    if number % 2 == 1:
#        print(True)
#        break
#else:
#    print(False)

## 3. Think about the return conditions of the loop

#count = 0
#for number in numbers:
#    if number % 2 == 1:
#        count += 1    # Count the odd numbers
#print(count > 0)      # Aha! a programmer who understands that Boolean
                      #    expressions are not just used in if statements!

## 4. do you want it shorter?
                      
#count = 0
#for number in numbers:
#    count += number % 2 == 1
#print(count > 0)
