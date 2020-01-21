# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:36:20 2020

@author: panch1t0
"""

aclNum=int(input("El nuermo de ACL es? "))
if aclNum >=1 and aclNum <= 99:
    print(" Es un ACL standard")
elif aclNum >=100 and aclNum <= 199:
    print(" Es un ACL extendido")
else:
    print(" No es estandar ni extendido")