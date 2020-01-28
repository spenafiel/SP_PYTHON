# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:27:00 2020

@author: CEC
"""

import numpy as np
import time 

a=np.array([1,2,3])
print(a)
#**************************************
b=np.array([(1,2,3),(4,5,6)])
print(b)
#**************************************



SIZE=1000000
L1= range(SIZE) #
L2= range(SIZE)
A1= np.arange(SIZE)  #
A2= np.arange(SIZE)

start= time.time()
result=[(time.time()-start)*1000]

start=time.time()
reult=A1+A2
print((time.time()-start)*1000)

#**************************************
#creR UN mATRIZ de unos -3 filas 4 columnas
unos = np.ones((3,4))
print(unos) #imprime 3 filas y 4 1 lista

#crear una matriz de ceros -3 filas 4 columna
ceros = np.zeros((3,4))
print(ceros)

#**************************************
#crer una matriz con valores aleatorios
aleatorios = np.random.random((2,2))
print(aleatorios)

#Crear una matriz vacía
vacia = np.empty((3,2))
print(vacia)

#Crear una matriz con un solo valor
full = np.full((3,2),8)
print(full)

# crear una matriz con valores espaciados uniformemente

espacio1 = np.arange(0,30,5)
print(espacio1)
#out put [ 0  5 10 15 20 25]

#**************
espacio2 = np.linspace(0,2,5)
print(espacio2)
#output [0.  0.5 1.  1.5 2. ]

#Crear una matriz identidad
identidad1 = np.eye(4,4)
print(identidad1)
#out put [[1. 0. 0. 0.]
# [0. 1. 0. 0.]
# [0. 0. 1. 0.]
# [0. 0. 0. 1.]]


identidad2 = np.identity(4)
print(identidad2)
#out put [[1. 0. 0. 0.]
# [0. 1. 0. 0.]
# [0. 0. 1. 0.]
# [0. 0. 0. 1.]]

#conocer las dimensiones de una matriz

a= np.array([(1,2,3),(4,5,6)])
print(a.ndim)
#out put 2 matrices

#conocer el tipo de los datos
a = np.array([(1,2,3)])
print(a.dtype)

#conocer el tamaño y forma d ela matriz
a = np.array([1,2,3,4,5,6])
print(a.size) #tamaño
print(a.shape) #forma


# cambio de forma de una matriz
a = np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)

# out put [[ 8  9]
# [10 11]
# [12 13]]


#
a = np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])
#out put 5

#MINIMO MAXIMO Y SUMA

a = np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())

#raiz cuadrada y la desviacion estandar de la matriz
a=np.array([(1,2,3),(3,4,5,)])
print("\n"*2)
print(np.sqrt(a))

#operaciones
x = np.array([(1,2,3),(3,4,5,)])
y = np.array([(1,2,3),(3,4,5,)])

print(x+y)
print("\n")
print(x-y)
print("\n")
print(x*y)
print("\n")
print(x/y)
print("\n")


































































































