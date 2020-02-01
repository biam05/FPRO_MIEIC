# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:43:03 2018

@author: biam05
"""

def wc(filename):
    file = open(filename)
    file2 = open(filename)
    file3 = open(filename)
    return (len(file.readlines()), len(file2.read().split()), len(list(file3.read())))