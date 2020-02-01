# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:07:57 2018

@author: biam05
"""

h = str(input("Tag: "))
text = str(input("String: "))

html = str("<") + h + str(">") + text + str("</") + h + str(">")

print(html)