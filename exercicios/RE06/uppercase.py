#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:13:58 2018

@author: up201806551
"""

def uppercase(astring):
    lower = astring.lower()
    lista_astring = list(enumerate(astring))
    lista_lower = list(enumerate(lower))
    if lista_lower[0] != lista_astring[0] or lista_lower[1] != lista_lower[1] or lista_lower[2] != lista_astring[2]:
        result = astring.upper()
    else:
        result = astring
    return result