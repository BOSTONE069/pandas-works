#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


d = {'a':[1,2,3,4,5],'b':[5,6,7,8,np.nan],'c':[0,1,3,np.nan,np.nan],'d':[3,4,np.nan,np.nan,np.nan],'e':[5,np.nan,np.nan,np.nan,np.nan]}


# In[4]:


d # this is a dictionary


# In[5]:


df = pd.DataFrame(d) # this is converting the dictionary into dataframe


# In[6]:


df


# In[7]:


df.dropna()#this is for droping a column or raw that has no value


# In[8]:


df.dropna(axis=0)#this is for accessing the raw that has all the values


# In[12]:


df.dropna(axis=1) #this is for accessing the column that has all the values


# In[13]:


df.dropna(thresh = 3)# this gives only rows where more that three values are available`


# In[14]:


df.fillna(1)# this ia for filling the missing values


# In[15]:


df['b'].fillna(value = df['b'].mean()) #this repalces the value with the mean of the values in that particular column


# In[16]:


df['c'].fillna(value = df['c'].mean())#this repalces the value with the mean of the values in that particular column


# In[17]:


df['e'].fillna(value = df['b'].mean())#this repalces the value with the mean of the values in that particular column


# In[18]:


df


# In[ ]:




