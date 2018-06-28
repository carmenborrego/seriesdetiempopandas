# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:01:43 2018

@author: carme
"""

import pandas as pd
xlsx=pd.ExcelFile('consultapib.xlsx')
print(xlsx.sheet_names)

df=xlsx.parse('Hoja1')
print(df)













