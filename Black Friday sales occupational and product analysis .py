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


sns.countplot(x = df['Stay_In_Current_City_Years'])


# In[6]:


sns.countplot(x = df['Stay_In_Current_City_Years'], hue = 'Gender', data = df)


# In[7]:


sns.countplot(x = df['Stay_In_Current_City_Years'], hue = 'Marital_Status', data = df)


# In[8]:


sns.countplot(x = df['Stay_In_Current_City_Years'], hue = 'City_Category', data = df)


# In[ ]:





# In[9]:


sns.countplot(x = df['Stay_In_Current_City_Years'], hue = 'Age', data = df)


# In[10]:


sns.countplot(x = df['Stay_In_Current_City_Years'], hue = 'Gender', data = df)


# In[11]:


df.groupby('Stay_In_Current_City_Years').sum()['Purchase']


# In[12]:


df.groupby('Stay_In_Current_City_Years').sum()['Purchase'].plot(kind = 'pie', autopct = "%.2f")


# In[13]:


df.groupby('Stay_In_Current_City_Years').sum()['Purchase'].plot(kind = 'bar')


# In[14]:


df.groupby('Stay_In_Current_City_Years').mean()['Purchase'].plot(kind = 'bar')


# In[15]:


sns.countplot(x = df['Occupation'])


# In[16]:


df.groupby('Occupation').size().plot(kind = 'bar')


# In[17]:


df.groupby('Occupation').size().sort_values().plot(kind = 'bar')


# In[18]:


df.groupby('Occupation').sum()['Purchase'].sort_values().plot(kind = 'bar')


# In[19]:


df.groupby('Occupation').mean()['Purchase'].sort_values().plot(kind = 'bar')


# In[20]:


df.groupby('Occupation').mean()['Purchase'].sort_values()


# In[21]:


df.groupby('Occupation').sum()['Purchase'].sort_values()


# In[22]:


sns.countplot(x = 'Occupation', hue = 'Marital_Status', data = df)


# In[23]:


sns.countplot(x = 'Occupation', hue = 'Gender', data = df)


# In[24]:


df.groupby('Occupation').nunique()['Product_ID']


# In[25]:


df.groupby('Product_Category_1').size()


# In[26]:


df.groupby('Product_Category_1').sum()['Purchase'].sort_values().plot(kind = 'bar')


# In[27]:


df.groupby('Product_Category_1').size().sort_values().plot(kind = 'bar')


# In[31]:


df.groupby('Product_Category_1').mean()['Purchase'].sort_values().plot(kind = 'bar')


# In[33]:


df.groupby('Product_ID').sum()['Purchase'].sort_values().nlargest(10).plot(kind = 'bar')


# In[35]:


df.groupby('Product_ID').mean()['Purchase'].sort_values().nlargest(10).plot(kind = 'bar')


# In[36]:


sns.countplot(x = 'Product_ID', hue = 'Gender' , data = df)


# In[37]:


sns.countplot(x = 'Product_Category_1', hue = 'Gender' , data = df)


# In[ ]:




