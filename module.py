# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:07:54 2020

@author: CEC
"""

#print("Quiero ser un modulo")

#if __name__=="__main__":
#      print("I prefer to be a module")
#else:
#      print("I like to be a module")
n = input('Introduce un numero: ')
n = int(n)

def fib(n):
    a, b =0 , 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
#fib(n)