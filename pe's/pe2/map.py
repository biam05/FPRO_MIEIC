# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:25:12 2019

@author: biam05
"""

def map(pos, steps):
    x = pos[0]
    y = pos[1]
    steps_list = steps.split('-')
    for step in steps_list:
        if step == 'up':
            y += 1
        elif step == 'left':
            x -= 1
        elif step == 'down':
            y -= 1
        elif step == 'right':
            x += 1
    final = x, y
    return tuple(final)