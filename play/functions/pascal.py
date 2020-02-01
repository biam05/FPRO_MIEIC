# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:44:55 2019

@author: biam05
"""

def pascal(n):
    result = ''
    
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)
    
    def valor(r, n):
        valor = int(factorial(n) / (factorial(n - r) * factorial(r)))
        return valor
        
    for linha in range(n):
        for r in range(linha + 1):
            result += str(valor(r, linha)) + ' '
        result += '\n'
        
    return result