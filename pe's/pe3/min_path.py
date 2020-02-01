# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:44:09 2019

@author: biam05
"""

def min_path(matrix, a, b, visited=[]):
    if a == b:                              # final position
        return 0
    if a[0] < 0 or a[0] >= len(matrix):     # outside matrix lines
        return 'IMPOSSIBLE'
    if a[1] < 0 or a[1] >= len(matrix[0]):  # outside matrix columns
        return 'IMPOSSIBLE'
    if matrix[a[0]][a[1]]:                  # an obstacle
        return 'IMPOSSIBLE'
    if a in visited:                        # already visited
        return 'IMPOSSIBLE'
    # find a min path
    mindist = 
    possible = [(0,1), (1,0), (1,1), (-1,-1), (-1,0), (-1,1), (0,-1), (1,-1)]
    for p in possible:
        l, c = a[0]+p[0], a[1]+p[1]
        # try the direction
        d = 1 + min_path(matrix, (l, c), b, visited+[a])
        # see if it's the best so far
        if d < mindist:
            mindist = d
    return mindist

mx = [
       [False]*4,
       [False, True, False, False],
       [False, True, False, False],
       [False]*4
     ]
print(min_path(mx, (2, 0), (0, 3)))