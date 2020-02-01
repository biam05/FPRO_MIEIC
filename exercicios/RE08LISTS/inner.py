# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:45:33 2018

@author: biam05
"""

def inner(u, v):
    produto_vetorial = []
    final = 0
    for i in range(len(u)):
        resultado = u[i] * v[i]
        produto_vetorial.append(resultado)
    final = sum(produto_vetorial)
    return final