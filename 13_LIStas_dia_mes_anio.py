# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:48:11 2020

@author: panch1t0
"""

def isYearLeap(year):
#
# Codigo from LAB Listas y return
    if year >=0 and year<=2020:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                    return True
        else:
            return False
    else:
        return None
#

def daysInMonth(year, month):
#
# put your new code here
#
#    print(isYearLeap(year))
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    res=dias[month-1]
    if month == 2 and isYearLeap(year):
        res=29
    return res 
def dayOfYear(year, month, day):
#
    suma=day
    for i in range (1,month):
        suma =suma+daysInMonth(year, i)
        print(i,daysInMonth(year, i))
    return suma
    
print(dayOfYear(2000, 7, 1))



