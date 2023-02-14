# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:28:57 2022

@author: axabadia
"""

#1. Import the export_import.csv file as a pandas dataframe. Name it df.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('export_import.csv')

#2. Delete the last three files.

df=df[0:29]
#3. Change the column titles to more understandable ones: Country, Exports, Imports, GDP and Population.

df.columns

df.rename(columns={'GEO/TIME':'Country', 'Exp_2016':'Exports',
		   'Imp_2016':'Imports', 'gdp_curr_2016':'GDP', 
		   'pop_2016': 'Population'},inplace=True)
#4. Change the name of Germany(until1990formerterritoryoftheFRG) to Germany

df.loc[4,'Country']='Germany'

#5. Put the column “Country” as the index fo the dataframe.
df=df.set_index('Country')

#6. Calculate exports over GDP, imports over GDP and imports per capita.
df['ExpGDP']=df['Exports']/df['GDP']
df['ImpGDP']=df['Imports']/df['GDP']
df['Impcap']=df['Imports']/df['Population']

#7. Sort the database in descending order according to the percentage of exports on GDP and assign it to df2.
df2=df.sort_values(by=['ExpGDP'],ascending=False)

#8. Take the 5 largest Countries acording to this percentage
list(df2.index)[0:5]

#9. Sort the database by the imports per capita and make a bar graph.
df3=df.sort_values(by=['Impcap'])
plt.bar(df3.index,df3['Impcap'])
plt.xticks(rotation='vertical')

#10. Select the countries with exports and imports over GDP greater than 60%.
df4=df[(df['ExpGDP']>0.7) & (df['ImpGDP']>0.7)]

#11. Create array df3 with these countries, containing the columns of exports/GDP and imports/GDP.
df4=df4[['ExpGDP','ImpGDP']]

#12. Draw the selected data.
plt.bar(df4.index,df4['ExpGDP'])
plt.bar(df4.index,df4['ImpGDP'])
plt.xticks(rotation='vertical')

import numpy as np 
import matplotlib.pyplot as plt 
  
X = df4.index
Y = df4.ExpGDP
Z = df4.ImpGDP
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Y, 0.4, label = 'Exp')
plt.bar(X_axis + 0.2, Z, 0.4, label = 'Imp')
  
plt.xticks(X_axis, X,rotation='vertical')
plt.xlabel("Countries")
plt.ylabel("Exports")
plt.title("Imports")
plt.legend()
plt.show()
