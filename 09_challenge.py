# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:27:22 2020

@author: panch1t0
"""

while True:
    varios=[input('Nombre: '),input('apellido: '),input('edad: '),input('location: ')]
    print("Hola",varios[0],varios[1],"de ",varios[2],"anios ","proveniente de ",varios[3])
    y=int(varios[2])
    if y>=0 and y<=10:
        print('Usted es un Ninio')
    elif y>=11 and y<=17:
        print ('Usted es un Adolecente')
    elif y>=18 and y<=40:
        print ('Usted es un Adulto')
    else:
        print ('Usted es un Adulto mayor')
    x=input("Continuar Y or N: ")
    if x == 'n' or x == 'N':
        print('salio')
        break