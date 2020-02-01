# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:06:12 2018

@author: biam05
"""

#
# DESCRIPTION of exercise 4: 
#
#    Write a Python function adigits that receives 3 strings, each one with a 
#    single character, representing a decimal digit.
#    The function should return the highest integer number that you can assemble 
#    with the 3 digits given as parameters.
#
#    For example: adigits("4", "2", "5") returns the integer 542
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def adigits(n1, n2, n3):
    """
    build the highest possible number out of the combination of 3 digits
    """
    #### MY CODE STARTS HERE ######################################
    number1 = str(n1) + str(n2) + str(n3)
    number2 = str(n1) + str(n3) + str(n2)
    number3 = str(n2) + str(n1) + str(n3)
    number4 = str(n2) + str(n3) + str(n1)
    number5 = str(n3) + str(n1) + str(n2)
    number6 = str(n3) + str(n2) + str(n1)
    number_list = [int(number1), int(number2), int(number3), int(number4), int(number5), int(number6)]
    result = max(number_list)
    return result
    #### MY CODE ENDS HERE ########################################