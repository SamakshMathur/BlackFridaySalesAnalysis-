#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 


# In[2]:


df = pd.read_csv('BlackFriday.csv')


# In[3]:


del df['Product_Category_2']
del df['Product_Category_3']


# In[5]:


df.head()


# In[7]:


df['User_ID'].nunique()


# In[8]:


df['User_ID'].unique()


# In[12]:


df['Age'].nunique()


# In[13]:


df['Age'].unique()


# In[14]:


df['Gender'].nunique()


# In[15]:


df['Gender'].unique()


# In[16]:


df['Occupation'].unique()


# In[19]:


df['Occupation'].unique()


# In[20]:


df['City_Category'].unique()


# In[21]:


df['Marital_Status'].unique()


# In[22]:


df['Purchase'].sum()


# In[24]:


mean_purchase = df['Purchase'].sum()/len(df['Purchase'])
mean_purchase


# In[29]:


for column in df.columns:
    print(column,'|',df[column].nunique(),'|',df[column].unique())


# In[ ]:




