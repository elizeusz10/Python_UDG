#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("export_import.csv")
#1


# In[3]:


df.drop(df.tail(3).index,inplace=True)
#2


# In[4]:


df.columns = ['Country', 'Exports', 'Imports', 'GDP' , 'Population']
#3


# In[5]:


df.loc[4, ["Country"]] = "Germany"
du=df

#4


# In[6]:


df = df.set_index("Country")
#5


# In[7]:


exports = df['Exports'].tolist()
GDP = df['GDP'].tolist()
imports= df['Imports'].tolist()
pop = df['Population'].tolist()
EoG = []
for x, y in zip(exports, GDP):
    c= float(x)/float(y)
    EoG.append(c)
IoG=[]
for x, y in zip(imports, GDP):
    c= float(x)/float(y)
    IoG.append(c)
IpC = []
for x, y in zip(imports, pop):
    c= float(x)/float(y)
    IpC.append(c)

df = df.assign(EoG=EoG)
df = df.assign(IoG=IoG)
df = df.assign(IpC=IpC)
du = du.assign(IpC=IpC)
#6


# In[8]:


df2 = df.sort_values('EoG', ascending=False)
#7


# In[9]:


Five_max = df2.head(5)
#8


# In[10]:


du = du.sort_values('IpC')
plt.bar(du['Country'], du['IpC'],)
plt.title('Country Vs IpC')
plt.xlabel('Country')
plt.ylabel('IpC')
plt.show()
#9


# In[11]:


filt = (df['IoG'] > 0.30) & (df['EoG'] > 0.30)
dp = df.loc[filt]
#10


# In[21]:


df3 = {}
df3 = pd.DataFrame(df3)
df3 = df3.assign(EoG=EoG)
df3 = df3.assign(IoG=IoG)
df3 = np.array(df3)
#11


# In[ ]:




