# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:18:04 2018

@author: biam05
"""

def calculator(expr):
    result = 0
    if isinstance(expr, int):
        return expr
    a = calculator(expr[0])
    b = calculator(expr[2])
    if expr[1] == '+':
        result += a + b
    elif expr[1] == '-':
        result += a - b
    elif expr[1] == '*':
        result += a * b
    return result

            