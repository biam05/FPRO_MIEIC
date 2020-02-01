# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:22:12 2019

@author: biam05
"""

def raise_exception(alist, value):
    lista = []
    for number in alist:
        if number <= value:
            erro = ValueError('{0} is not greater than {1}'.format(number, value))
            lista.append(erro)
    return lista

print(raise_exception([1, -2, 3, 0], 3))