# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:26:58 2018

@author: biam05
"""

def palindrome_index(s):
    inverse = s[::-1]
    final = ''
    print(inverse)
    for i in range (len(s)-1):
        
        if s[:i:] == inverse[::]:
            final = i
        else:
            final = ''
    if final == '' :
        return -1
    else: 
        return final
        

                
        
    


        
            