# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
# DESCRIPTION of exercise 2: 
#
#   Write a program that takes a single integer n provided by the user and returns True, 
#   when it is a prime number, and False otherwise.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def is_prime():
    result = "Not yet implemented"
    
    #### MY CODE STARTS HERE ############################
    n = int(input())
    divisor_list = []
    for i in range (1, n+1):
        if (n % i) == 0:
            divisor_list.append(i)
        if len(divisor_list) == 2:
            result = True
        else:
            result = False
    #### MY CODE ENDS HERE ##############################
    
    return result
