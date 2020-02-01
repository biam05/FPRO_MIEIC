# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:16:37 2018

@author: biam05
"""

#
# DESCRIPTION of exercise 5: 
#
#   Write a function mastermind to evaluate a single line of a mastermind game.
#   The function receives 6 single character strings. 
#   Each string can be "b" for blue, "w" for white and "y" for yellow.
#   The first 3 arguments are the user guess. The last 3 arguments are the correct key. 
#   Argument 1 is the user guess for the value at argument 4 and so on. 
#   You should give 3 points for each user guess that is completely correct, that is, 
#   same color at the same position in the key and 1 point if the user guessed the color right 
#   but at the wrong position (that is, the color exists in the key but at another wrong position).
#
#   For example: mastermind("b", "w", "y", "b", "w", "y") returns the integer 9
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def mastermind(g1, g2, g3, c1, c2, c3):
    """
    evaluate a line of the mastermind game
    """
    #### MY CODE STARTS HERE ######################################
    result = 0
    guess = str(g1), str(g2), str(g3)
    code = str(c1), str(c2), str(c3)
    code_list = [c1, c2, c3]
    if guess == code:
        result = 9
    else:
        if g1 == c1:
            result += 3
        else: 
            if g1 in code_list:
                result += 1
        if g2 == c2:
            result += 3
        else: 
            if g2 in code_list:
                result += 1
        if g3 == c3:
            result += 3
        else: 
            if g3 in code_list:
                result += 1
    return result
    #### MY CODE ENDS HERE ########################################