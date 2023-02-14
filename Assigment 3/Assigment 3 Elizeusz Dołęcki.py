#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
df['GDPcap']= df['GDP']/df['Population']
#2 ass3

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


# In[2]:


df['GDPcap'].quantile(.33)
#3


# In[3]:


df['GDPcap'].quantile(0.66)
#3


# In[4]:


df['level']='medium'
df.loc[df['GDPcap'] < 16.070624104853408, 'level' ] = 'poor'
df.loc[df['GDPcap'] > 34.77678142873976 , 'level' ] = 'rich'
#3


# In[5]:


df = df.sort_values('GDPcap')
q = df[['ExpGDP', 'ImpGDP']].mean()
w = df[['ExpGDP', 'ImpGDP']].max()
e=df[['ExpGDP', 'ImpGDP']].min()
r=df[['ExpGDP', 'ImpGDP']].var()
t=df[['ExpGDP', 'ImpGDP']].std()
#4


# In[6]:


freshwater = pd.read_excel('API_4570336.xls')
co2=pd.read_excel('API_4701187.xls')
#5


# In[7]:


DB = freshwater[['Country Name', '2018']] 
pd.DataFrame(DB)
DB['2018co2']=  co2['2018']
#6


# In[8]:


DB.rename(columns = {'Country Name': 'Country'}, inplace = True)
df = df.reset_index()
DF2 = pd.merge(df, DB, how='left')
DF2
#7


# In[9]:


DF2.loc[8, ['2018', '2018co2']] =[0.5565, 33000]
DF2.loc[11, ['2018', '2018co2']] =[1.591, 100900.0015]
DF2.loc[19, ['2018', '2018co2']] =[8.419, 360730.011]
#8


# In[10]:


DF2['EmiCap']= DF2['2018co2']/DF2['Population']
DF2['WatCap']= DF2['2018']/DF2['Population']
#9


# In[11]:


max_co2 = DF2.loc[DF2['2018co2'].idxmax()]
max_co2
#9


# In[12]:


min_wat = DF2.loc[DF2['2018'].idxmin()]
min_wat
#9


# In[13]:


filt = DF2['level'] == 'rich'
DF8 = DF2.loc[filt]
x = DF8['2018co2'].sum()
y= DF8['Population'].sum()
AverRich=x/y
AverRich
#10


# In[14]:


filt = DF2['level'] == 'medium'
DF9 = DF2.loc[filt]
a = DF9['2018co2'].sum()
b= DF9['Population'].sum()
AverMed=a/b
AverMed
#10


# In[15]:


filt = DF2['level'] == 'poor'
DF0 = DF2.loc[filt]
m = DF0['2018co2'].sum()
n= DF0['Population'].sum()
AverPoor=m/n
AverPoor
#10


# In[17]:


#Countries with the highest GDP per capita have the highest index of emission co2 per capita. Further are countries from 'poor' category. At the end are countreis with 'medium'.


# In[ ]:




