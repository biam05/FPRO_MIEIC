# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:46:03 2019

@author: biam05
"""

tS = float(input('Swimming time:'))
tC = float(input('Cycling time:'))
tR = float(input('Running time:'))

if tS + tC + tR >= 4:
    print('Time')
else:
    if 1.5 / tS < 2:
        print('Swimming')
    else:
        if 40/tC < 20:
            print('Cycling')
        else:
            if 10/tR < 8:
                print('Running')
            else:
                print(tS + tC + tR)