#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


plik_1= pd.read_excel("gdp.xlsx")


# In[3]:


Zone=plik_1["Zone"].tolist()
GDP=plik_1["GDP"].tolist()
Population= plik_1["Population"].tolist()


# In[4]:


plik_1 = plik_1.dropna()
#1


# In[5]:


Zone=plik_1["Zone"].tolist()
GDP=plik_1["GDP"].tolist()
Population= plik_1["Population"].tolist()  
#1


# In[6]:


plik_1.shape
#2


# In[7]:


print(Zone[-4:])
#3


# In[8]:


plik_1.loc[81:82, ['GDP']] = [9080.51,3154.65]
#4


# In[9]:


Zone=plik_1["Zone"].tolist()
GDP=plik_1["GDP"].tolist()
Population= plik_1["Population"].tolist()
#4


# In[10]:


filt = plik_1['Population'] == 0
#5


# In[11]:


plik_1 = plik_1.drop(index=plik_1[filt].index)
#5


# In[12]:


Zone=plik_1["Zone"].tolist()
GDP=plik_1["GDP"].tolist()
Population= plik_1["Population"].tolist()
#5


# In[13]:


suma=0
for x in GDP:
    suma=suma+x
print(suma)
#6 the score is in milions


# In[14]:


P=[]
for x, y in zip(GDP, Population):
    c= float(x)/float(y)
    P.append(c)
#7


# In[15]:


min(P)
#7


# In[16]:


over = []
for a in GDP:
    if a > 100000:
        b = GDP.index(a)
        over.append(Zone[b])
print(over)
#8

