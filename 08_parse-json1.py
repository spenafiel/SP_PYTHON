# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 08:57:23 2020

@author: CEC
"""

import urllib.parse
import requests

main_api ="https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "FDAlkhd7R3Z1dx7kYOH34jF5GNDUbM7W"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)


#******************************************************************

