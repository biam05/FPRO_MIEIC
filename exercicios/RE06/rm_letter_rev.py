#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:49:06 2018

@author: up201806551
"""
def rm_letter_rev(l, astr):
    result = ''
    cuts = astr.split(l)
    for i in range(len(cuts)):
        result += cuts[i]
    result = result[::-1]
    return result