# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:05:01 2018

@author: biam05
"""

#
# DESCRIPTION of exercise 6: 
#
#   Write a program that given an integer in the variable num, provided by the user,
#   computes its reverse (the number with the digits by the reverse order).
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def capicua():
    result = "Not yet implemented"

    #### MY CODE STARTS HERE ############################
    num = int(input(""))
    x = num
    inverse = ""
    while x > 0:
        inverse += str(x % 10)
        x = x - (x % 10)
        x = int(x / 10)
    num = str(num)
    inverse = str(inverse)
    if int(inverse) == int(num):
        result = num + " is a palindrome."
    else:
        result = num + " is not a palindrome."    
    #### MY CODE ENDS HERE ##############################
    
    return result