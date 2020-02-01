# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:59:07 2019

@author: biam05
"""

def rec_exceptions(l):
    lista = []
    for function in l:
        try:
            r = function()
        except Exception as ex:
            lista.append(ex)
        else:
            lista += rec_exceptions(r)
    return lista