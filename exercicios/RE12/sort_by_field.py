# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:26:02 2018

@author: biam05
"""

def sort_by_field(filename, field):
    textresult = ''
    file = open(filename, 'r')
    content = file.readlines()
    if content != []:
        for i in range(len(content)):
            content[i] = content[i].split(',')
        content[len(content)-1][len(content[len(content)-1])-1] += '\n'
        content[0][len(content[0])-1] = content[0][len(content[0])-1][:len(content[0][len(content[0])-1])-1]
        sortindex = content[0].index(field)
        newcontent = sorted(content[1:], key = lambda x: x[sortindex])
        newcontent.insert(0, content[0])
        newcontent[len(newcontent)-1][len(newcontent[len(newcontent)-1])-1] = newcontent[len(newcontent)-1][len(newcontent[len(newcontent)-1])-1][:len(newcontent[len(newcontent)-1][len(newcontent[len(newcontent)-1])-1])-1]
        newcontent[0][len(newcontent[0])-1] += '\n'
        for i in range(len(newcontent)):
            newcontent[i] = ','.join(newcontent[i])
        textresult = ''
        for i in range(len(newcontent)):
            textresult += ''.join(newcontent[i])
    return textresult