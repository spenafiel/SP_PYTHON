# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:18:29 2020

@author: CEC
"""

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong")
    
print("3")

#*******************************************************

try:
    x=int(input("Numero:"))
    y= 1 /x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong")
print("THE END")

#*******************************************************

try:
   # y= 0 /1
   y= 1 /0
except ZeroDivisionError:
    print("Zero Division")
except ArithmeticError:
    print("Arithmetic problem")
print("THE END.")

#*******************************************************

def badFun(n):
    try:
        return 1/n
    except ArithmeticError:
        print("Aritmetic Problem")
    return None
badFun(0)
print("THE END")

#*******************************************************
import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)


#*******************************************************

def validarNumero(prompt, min, max):
    while (True):
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("El valor debe estar dentro del RANGO --> (-10..10) <--")
    
v = validarNumero("Ingrese un valor desde -10 a 10:", -10, 10)

print("El número es:", v)
    









































