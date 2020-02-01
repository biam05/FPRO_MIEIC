# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:22:27 2018

@author: biam05
"""

import datetime

time = datetime.datetime.now()
time.minute
time.hour
hours = (time.hour + 8 + (time.minute + 30)//60) % 24
minutes = (time.minute + 30) % 60
print("Alarm set to", hours , ":", minutes)
