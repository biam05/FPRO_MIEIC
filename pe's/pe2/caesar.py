# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 23:27:54 2019

@author: biam05
"""

def caesar(message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sequence = []
    converter = []
    new_string = ''
    import math
    for i in range(len(message)):
        sequence.append(int(((1 + math.sqrt(5))**i-(1-math.sqrt(5))**i)/(2**i * math.sqrt(5))))
    for i in range(len(message)):
        tup = (message[i], sequence[i])
        converter.append(tup)
    for letter, number in converter:
        if letter not in alphabet:
            new_string += letter
        else:
            new_string += alphabet[(alphabet.find(letter) - number)%26]
    return new_string