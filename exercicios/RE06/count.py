#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:30:45 2018

@author: up201806551
"""

def count(word, phrase):
    result = 0
    word_list = phrase.split()
    for i in range (len(word_list)-1):
        if word.lower() in word_list[i]:
            result += 1    
    return result