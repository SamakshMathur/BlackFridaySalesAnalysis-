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


# In[6]:


for column in df.columns: 
    print(df[column].nunique(),':',column)


# In[13]:


Gender = pd.DataFrame({'Ratio' : [len(df[df['Gender'] == 'M']),len(df[df['Gender'] == 'F'])]},index = ['Male','Female']) 
Gender
Gender.plot.pie(y = 'Ratio', figsize = (6,6), autopct = "%.2f")


# In[15]:


df.groupby('Gender').size().plot(kind = 'pie', autopct = "%.2f")


# In[18]:


df.groupby('Gender').size().plot(kind = 'bar', figsize = (6,6))


# In[22]:


# how much total money male and female are spending in shopping
df.groupby('Gender').sum()['Purchase']


# In[25]:


df.groupby('Gender').sum()['Purchase'].plot(kind = 'pie', autopct = "%.2f")


# In[24]:


# how much average money male and female are spending in shopping
df.groupby('Gender').mean()['Purchase'] 


# In[26]:


df.groupby('Gender').mean()['Purchase'].plot(kind = 'pie', autopct = '%.2f')


# In[ ]:




