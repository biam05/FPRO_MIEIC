# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:56:55 2018

@author: biam05
"""

def remove_leading(ip):
    ip_sliced = ip.split('.')
    ip = ''
    number = ''
    for i in ip_sliced:
        if i == '0':
            number = '0'
        else:
            for j in range i:
                if j == '0':
                    pass
                else:
                    number += j
    ip = 
    ip 
    return ip