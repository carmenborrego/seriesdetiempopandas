# seriesdetiempopandas
manejo de series de tiempo con pandas de python

import pandas as pd
xlsx=pd.ExcelFile('consultapib.xlsx')
print(xlsx.sheet_names)

df=xlsx.parse('Hoja1')
print(df)
