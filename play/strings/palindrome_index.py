# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:06:40 2019

@author: biam05
"""

def palindrome_index(s):
    
    def is_palindrome(string):
        if string == string[::-1]:
            return True
        else:
            return False
    if s == s[::-1]:
        return -1
    
    for i in range(len(s)):
        new_string = s[:i] + s[i+1:]
        if is_palindrome(new_string) == True:
            return i
    return -1