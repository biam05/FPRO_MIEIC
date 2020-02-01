# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 23:18:14 2019

@author: biam05
"""
def f_order(elem):
    name, relationship = elem
    order = ('sibling', 'parent', 'cousin', 'grandparent').index(relationship)
    
    return order, name

def genealogy(l):
    return sorted(l, key = f_order)




print(genealogy([('carlos', 'sibling'), ('paulo', 'sibling'), ('maria',
'parent'), ('pedro', 'parent'), ('alfredo', 'cousin'), ('carla',
'cousin'), ('artur', 'grandparent'), ('geraldes', 'grandparent'),
('matilde', 'grandparent')]))