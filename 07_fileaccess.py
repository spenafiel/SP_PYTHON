# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:05:13 2020

@author: CEC
"""

file = open("devices.txt","r")
for item in file:
    print(item)
file.close()

#******************************************
devices=[]
file = open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)

#******************************************

file = open("devices.txt","a")
while True:
       newitem = input('Texto Nuevo:')
       if newitem =='exit':
           print('All done')
           break
       file.write(newitem + "\n")
   
file.close()


#******************************************

    

