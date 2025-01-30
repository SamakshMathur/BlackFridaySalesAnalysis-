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


# In[4]:


df.head()


# In[10]:


df.groupby('Age').size().plot(kind = 'bar', figsize = (12,6), title = 'Purchase distribution by age')


# In[26]:


lst = []
for i in df['Age'].unique():
    lst.append([i ,df[df['Age'] == i]['Product_ID'].nunique()])
    
    
data = pd.DataFrame(lst , columns = ['Age','Products'])


# In[33]:


data.plot.bar(x = 'Age')


# In[36]:


df.groupby('Age').sum()['Purchase'].plot(kind = 'bar', figsize = (6,6), title = 'total amount spent by age distribution')


# In[38]:


df.groupby('Age').mean()['Purchase'].plot(kind = 'bar', figsize = (6,6), title = 'average amount spent by age distribution')


# In[40]:


df.groupby('Age').mean()['Purchase'].plot(kind = 'pie', figsize = (6,6), title = 'average amount spent by age distribution', autopct = "%.2f")


# In[46]:


df.groupby('Marital_Status').size().plot(kind = 'pie', figsize = (6,6), autopct = "%.2f")


# In[ ]:





# In[42]:


df.groupby('Age').sum()['Marital_Status']


# In[ ]:





# In[ ]:




