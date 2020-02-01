# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:10:01 2019

@author: biam05
"""

#def no_consecutives1(k):
#    count = 0
#    binarios = []
#    
#    def check_consecutives(n):
#        ones = 0
#        for algarismo in n:
#            if algarismo == '1':
#                ones += 1
#            elif algarismo == '0':
#                ones = 0
#            if ones > 1:
#                return False
#        return True
#    
#    for i in range(2**k):
#        number = str(bin(i))[2:]
#        binarios.append(number.zfill(k))
#    for binario in binarios:
#        if check_consecutives(binario):
#            count += 1   
#    return count

def no_consecutives1(k):
    binary_numbers = []
    for i in range(2**k):
        binary_numbers.append(bin(i)[2:])
    counter = 0
    for i in binary_numbers:
        if '11' not in i:
            counter += 1
    return counter
