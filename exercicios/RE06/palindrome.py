# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:39:59 2018

@author: biam05
"""

def palindrome(astring):
    final = 0
    substring = ''
    for i in range(0, (len(astring) - 1)):
        for j in range(i+1, (len(astring)+1)):
            substring = astring[i:j]
            if len(substring) > 1:
                invstring = substring[::-1]
                if invstring == substring:
                    final += 1
    result = "For string '" + astring + "': " + str(final) + " palindrome substrings"
    return result

