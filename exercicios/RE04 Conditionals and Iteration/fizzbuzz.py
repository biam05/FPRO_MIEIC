# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:37:08 2018

@author: biam05
"""

#
# DESCRIPTION of exercise 3: 
#
#   Write a Python program which “plays” the known game FizzBuzz over a sequence of integers 
#   from 0 to an integer n provided by the user. 
#   See Google Docs for implementation details.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def fizz_buzz():
    result = "Not yet implemented"
    
    #### MY CODE STARTS HERE ############################
    n = int(input())
    for i in range(n):
        if (i % 3) == 0 and (i % 5) == 0:
            result = ""
        else:
            if (i % 3) == 0:
                result += str("Fizz ")
            else:
                if (i % 5) == 0:
                    result += str("Buzz ")
                else:
                    result += str(i)
                    result += " "
    if (n % 3) == 0 and (n % 5) == 0:
        result += ""
    else:
        if (n % 3) == 0:
            result += str("Fizz")
        else:
            if (n % 5) == 0:
                result += str("Buzz")
            else:
                result += str(n)
    #### MY CODE ENDS HERE ##############################
    
    return result