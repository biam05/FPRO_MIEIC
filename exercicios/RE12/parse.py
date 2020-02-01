# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 16:26:15 2018

@author: biam05
"""

def parse(filename):
    from ast import literal_eval as l_eval
    file = open(filename, 'r')
    content = file.read()
    content = content.split()
    contstr = ''
    for i in range(len(content)):
        if content[i][0] != '(':
            content[i] += ',' 
    for i in range(len(content)):
        contstr += content[i]
    return l_eval(contstr)