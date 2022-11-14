#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
from sympy import *


# In[2]:


A = np.array([[10,1,-1,8],[0,0,3,0],[1,2,4,1],[1,3,-5,8]])
B = np.array([[1,2,2,-1],[1,1,-1,1],[0,-1,-3,2]])
C = np.array([[1,2,1],[-1,1,2],[-1,0,-3]])
#1a


# In[3]:


D = A[1:4]
#1b


# In[4]:


try:
    F=A*D
except Exception:
    print("That's impossible")
#1c


# In[5]:


DT = np.transpose(D)
DT
#1c


# In[6]:


Id = np.identity(4)
G=np.dot(A,Id)
G
#1c


# In[7]:


Br = np.linalg.matrix_rank(B)
Br
#1d


# In[8]:


try:
    np.linalg.inv(C)
except:
    print("That's impossible")
#1e


# In[20]:


Province = ['02Albacete','03Alicante/Alacant','04Almería','01Araba/Álava','33Asturias','05Ávila','06Badajoz','07Balears,Illes','08Barcelona','48Bizkaia','09Burgos','10Cáceres','11Cádiz','39Cantabria','12Castellón/Castelló','13CiudadReal','14Córdoba','15Coruña,A','16Cuenca','20Gipuzkoa','17Girona','18Granada','19Guadalajara','21Huelva','22Huesca','23Jaén','24León','25Lleida','27Lugo','28Madrid','29Málaga','30Murcia','31Navarra','32Ourense','34Palencia','35Palmas,Las','36Pontevedra','26Rioja,La','37Salamanca','38SantaCruzdeTenerife','40Segovia','41Sevilla','42Soria','43Tarragona','44Teruel','45Toledo','46Valencia/València','47Valladolid','49Zamora','50Zaragoza','51Ceuta','52Melilla']
np.array(Province)


# In[21]:


Population = [387735, 1904362, 723899, 329856, 1006193, 159062, 667000, 1223961, 5641485, 1133833, 353021, 386302, 1259339, 584407, 578506, 489950, 777414, 1120185, 198842, 713583, 776944, 929968, 266471, 532865, 222329, 622617, 452219, 437260, 324419, 6769113, 1711693, 1522640, 659232, 304104, 157340, 1153633, 942849, 315896, 326506, 1098831, 153812, 1960257, 89176, 823721, 133118, 707078, 2589308, 517758, 167846, 959140, 82533, 83196]
np.array(Population)
#2a


# In[11]:


Over = []


# In[12]:


Pop = np.argwhere(Population>1000000)


# In[13]:


for x in Pop:
    Over.append(Province[x])


# In[14]:


Over = np.array(Over)


# In[15]:


Over 
#2b


# In[16]:


P = np.array([[1,2,-1],[0,2,3],[-1,0,4]])
S = np.array([2,-1,-1])
try:
    X2 = np.linalg.solve(P,S)
except Exception:
    R=np.array([[1,2,-1,2],[0,2,3,-1],[-1,0,4,-1]])
    if np.linalg.matrix_rank(P, tol=None, hermitian=False) == np.linalg.matrix_rank(R, tol=None, hermitian=False):
        print("There's infinity numbers of solutions")
    else:
        print("This is incompatible system")  
#3


# In[17]:


# y=100L - 0.0004L**2 


# In[18]:


y,L=symbols ('y  L')
Pb = 1.65*y - y 
# 4a
y=100*L - 0.0004*L**2
diff(y,L)

s=solve([diff(y,L)], [L])

y_1=100*s[L] - 0.0004*s[L]**2
#4b_1


# In[19]:


Pb = 1.65 *y_1  - y_1
Pb 
#4b_2

