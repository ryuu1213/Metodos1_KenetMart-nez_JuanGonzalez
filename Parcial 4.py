#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


df = pd.read_csv("https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/DataRotacion.csv")

df.drop(df[(df['angle'] != 30)].index, inplace=True)
data = np.array(df)
data


# In[5]:


"""
def GetModel(x,p):
    
    y = 0
    for n in range(len(p)):
        y += p[n]*x**n
    
    #y = p[0]*np.exp(p[1]*x)
        
    return y
"""

def y(h, lamb, w, g):
    return 2*np.sqrt(2)*w*np.cos(lamb*np.pi/180)*np.sqrt((h**3)/g)/3


# In[ ]:




