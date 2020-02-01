#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 08:22:23 2018

@author: jlopes

Code adapted from the book:

Brad Miller and David Ranum, Learning with Python: Interactive Edition
"""

##### step 1

#current_time = input("what is the current time (in hours)?")
#wait_time = input("How many hours do you want to wait")
#
#print(current_time)
#print(wait_time)

##### step 2

#final_time = current_time + wait_time
#print(final_time)

##### step 3

current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)

##### step 4

final_answer = final_time_int % 24
#
print("The time after waiting is: ", final_answer)

##### testing
# it is important to test your code on a range of inputs 
# It is especially important to test your code on boundary conditions (0, 23)
