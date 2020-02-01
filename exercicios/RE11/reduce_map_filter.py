# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:17:07 2018

@author: biam05
"""

def reduce_map_filter(args):
    from functools import reduce
    
    if isinstance(args, list): #condição base
        return args
        
    a = reduce_map_filter(args[2]) #recursão
    
    if args[0] == 'map':
        return list(map((args[1]), a))
    elif args[0] == 'filter':
        return list(filter((args[1]), a))
    elif args[0] == 'reduce':
        return reduce((args[1]), a)