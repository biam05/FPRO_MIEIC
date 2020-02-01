#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:49:05 2018

@author: up201806551
"""

def formal(name):
    result = ''
    result2 = ''
    names = name.split()
    result1 = names[len(names)-1] + ','
    first_names = names[0:len(names)-1]
    for i in range(len(first_names)):
        palavra = first_names[i]
        sigla = palavra[0] + '.'
        result2 += ' ' + sigla
    result = result1 + result2
    return result

