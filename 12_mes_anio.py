# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:44:19 2020

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
    if month==2 and isYearLeap(year):
        res=29
    return res 
testYears = [1900, 2000, 2016, 1987,400,2019]
testMonths = [2, 2, 2, 11,2,12]
testResults = [28, 29, 29, 30,29,31]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK", result)
	else:
		print("Failed", result)

        
        
        