#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns


# In[2]:


df = pd.read_csv('BlackFriday.csv')


# In[3]:


del df['Product_Category_2']
del df['Product_Category_3']


# In[4]:


df.head()


# In[5]:


df.groupby('Age').size().plot(kind = 'bar', title = 'Purchase distribution by AGE')


# In[6]:


sns.set(rc = {'figure.figsize':(12,6)})
sns.countplot(x = 'Age', hue = 'Gender', data = df)


# In[7]:


sns.set(rc = {'figure.figsize':(12,6)})
sns.countplot(x = 'Gender', hue = 'Age', data = df)


# In[8]:


sns.set(rc = {'figure.figsize':(6,6)})
sns.countplot(x = 'Gender', hue = 'Marital_Status', data = df)


# In[9]:


sns.set(rc = {'figure.figsize':(6,6)})
sns.countplot(x = 'Marital_Status', hue = 'Age', data = df)


# In[10]:


sns.set(rc = {'figure.figsize':(6,6)})
sns.countplot(x = 'Marital_Status', hue = 'Gender', data = df)


# In[16]:


sns.histplot(x = df['City_Category'])


# In[17]:


df.groupby('City_Category').size().plot(kind = 'pie',autopct = "%.2f")


# In[19]:


sns.countplot(x = 'City_Category', hue = 'Age', data = df)


# In[20]:


sns.countplot(x = 'Age', hue = 'City_Category', data = df)


# In[21]:


sns.countplot(x = 'Marital_Status', hue = 'City_Category', data = df)


# In[22]:


sns.countplot(x = 'City_Category', hue = 'Gender', data = df)


# In[24]:


df.groupby('City_Category').sum()['Purchase'].plot(kind = 'bar')


# In[25]:


df.groupby('City_Category').sum()['Purchase'].plot(kind = 'pie', autopct = "%.2f")


# In[26]:


df.groupby('City_Category').mean()['Purchase'].plot(kind = 'pie', autopct = "%.2f")


# In[ ]:




