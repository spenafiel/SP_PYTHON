# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:12:57 2020

@author: panch1t0
"""

while True:
    x=input("Ingrese un numero hasta cuanto contar: ")
    if x == 'q' or x == 'quit':
        print('salio')
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break