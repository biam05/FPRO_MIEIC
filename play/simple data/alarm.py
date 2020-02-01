# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:17:48 2019

@author: biam05
"""

def alarm(hour, minutes):
    mins = (51 + minutes)%60
    hours = (6 + hour + (51+minutes)//60)%24
    if mins < 10:
        mins = '0' + str(mins)
    if hours < 10:
        hours = '0' + str(hours)
    return '{0}:{1}'.format(hours, mins)

    