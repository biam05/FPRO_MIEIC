# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:30:55 2019

@author: biam05

"""

num = input('Choose a number:')

new_num = int(num[0])**3 + int(num[1])**3 + int(num[2])**3

if int(new_num) == int(num):
    print(True)
else:
    print(False)