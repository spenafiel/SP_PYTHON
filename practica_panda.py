# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:24:39 2020

@author: CEC
"""

import numpy as np
import pandas as pd
data = np.array([['','Col1','Col2'], ['Fila1',11,22], ['Fila2',33,44]])          
print(pd.DataFrame(data = data[1:,1:], index = data[1:,0], columns = data[0,1:]))