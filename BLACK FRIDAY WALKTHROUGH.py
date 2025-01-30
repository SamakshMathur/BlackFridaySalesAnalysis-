#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 
import numpy as np
from sklearn.impute import SimpleImputer


# In[2]:


df = pd.read_csv('BlackFriday.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df


# In[6]:


df.isnull().sum()


# In[9]:


df.dropna().isnull().sum()


# In[10]:


del df['Product_Category_2']
del df['Product_Category_3']


# In[11]:


df.head()


# In[ ]:




