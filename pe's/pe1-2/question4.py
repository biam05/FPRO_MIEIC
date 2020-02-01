# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:17:55 2019

@author: biam05
"""

A = input('Player A:')
B = input('Player B:')

if A == 'rock':
    if B == 'scissors':
        print('The winner is A')
    elif B == 'paper':
        print('The winner is B')
    elif B == 'rock':
        print('That\'s a draw')
elif A == 'scissors':
    if B == 'scissors':
        print('That\'s a draw')
    elif B == 'paper':
        print('The winner is A')
    elif B == 'rock':
        print('The winner is B')   
elif A == 'paper':
    if B == 'scissors':
        print('The winner is B')
    elif B == 'paper':
        print('That\'s a draw')
    elif B == 'rock':
        print('The winner is A')   
        