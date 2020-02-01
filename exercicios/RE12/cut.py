# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:16:00 2018

@author: biam05
"""

def cut(filename,delimiter, field):
    file = open(filename)
    lista = file.readlines()
    newlist = []
    for i in lista:
        newlist.append(i.split(delimiter))
    result = ''
    if isinstance(field, list):
        for i in range(len(newlist)):
            for j in field:
                result += newlist[i][j-1].split('\n')[0] + delimiter
            result = result[:len(result)-1]
            result += '\n'
    else:
        for i in range(len(newlist)):
            result += (newlist[i][field-1]).split('\n')[0] + '\n'
    return result[:len(result)-1]