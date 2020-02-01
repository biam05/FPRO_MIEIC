# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:46:12 2018

@author: biam05
"""

#
# DESCRIPTION of exercise 4: 
#
#   Write a program that checks if a triangle is equilateral, isosceles or scalene, 
#   with the 3 sides provided by the user, each one in different an input() statement. 
#   See Google Docs for implementation details.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def triangle_form():
    result = "Not yet implemented"
    
    #### MY CODE STARTS HERE ############################
    x = int(input(" "))
    y = int(input(" "))
    z = int(input(" "))
    if ((x + y) <= z) or ((x + z) <= y) or ((y + z) <= x):
        result = "Not a triangle"
    else:
        if (x == y) and (y == z):
            result = "Equilateral"
        else:
            if (x == z) or (y == z) or (x == y):
                result = "Isosceles"
            else:
                result = "Scalene"
    #### MY CODE ENDS HERE ##############################
    
    return result
