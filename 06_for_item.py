# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:00:11 2020

@author: panch1t0
"""

routers=["R1","R2","R3","R4","S1","S2","S3","FW1"]
switches=[]
for item in routers:
    if "S" in item:
        switches.append(item)