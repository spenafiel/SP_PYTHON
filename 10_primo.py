# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 22:55:38 2020

@author: panch1t0
"""

def primo(m):
   ban=True
   for i in range (2,n):
        if n%i==0:
            ban=False
            break
   if ban==True:
        print('Es PRIMO',m)
        return True
   else:
        print('NO Es PRIMO',m)       
        return False

n=input('Ingrese un numero ')
n=int(n)
print(primo(n))