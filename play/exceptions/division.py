# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:38:11 2019

@author: biam05
"""

def division(a, b):
    try:
        result = a / b
        return '{0}/{1} = {2}'.format(a, b, result)
    except ZeroDivisionError:
        return 'can\'t divide by 0!'
    except TypeError:
        return 'unsupported operand type(s) for division'

print(division(10,'b'))