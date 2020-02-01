# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 08:47:38 2018

@author: biam05
"""

n = int(input("Integer: "))
final = ''
for i in range (0, (n+1)):
    if (i % 5) == 0 and (i % 3) == 0:
        final += ''
    elif (i % 3) == 0:
        final += str('Fizz ')
    elif (i % 5) == 0:
        final += str('Buzz ')
    else:
        final += str(i)
        final += ' '
if (n % 5) == 0 and (n %3) == 0:
    final += ''
elif (n % 3) == 0:
    final += str("Fizz")
elif (n % 5) == 0:
    final += str("Buzz")
    

print(final)