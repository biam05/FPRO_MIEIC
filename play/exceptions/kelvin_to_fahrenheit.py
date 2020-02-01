# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:11:59 2019

@author: biam05
"""

def kelvin_to_fahrenheit(temp):
       assert temp >= 0, 'Colder than absolute zero!' 
       return int(1.8 *(temp - 273) + 32)