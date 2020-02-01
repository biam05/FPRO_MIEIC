# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:17:26 2019

@author: biam05
"""

def remove_leading(ip):
    ip_sliced = ip.split('.')
    ip = ''
    for i in ip_sliced:
        number = int(i)
        ip += str(number) + '.'
    ip = ip[:len(ip)-1]
    return ip

print(remove_leading("192.168.0.24"))