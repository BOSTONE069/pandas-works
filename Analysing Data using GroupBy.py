#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


# In[8]:


import pandas as pd


# In[13]:


p = {'item':['apple','apple','orange','orange','guns','guns'],'days':['Mon','Tue','Wed','Thu','Fri','Sat'],'sale':[200,100,80,200,100,5]}


# In[14]:


p


# In[16]:



df = pd.DataFrame(p)


# In[17]:


df


# In[18]:


x = df.groupby('item')# this groups the elements into there recurring categories


# In[19]:


x.mean() #this is calculating the mean of the elements


# In[20]:


x.max() #this is for calculating the maximum from the data


# In[21]:


x.min()#this is for calculating the minimum from the data


# In[22]:


x.sum() #this is for calculating the sum from the data


# In[23]:


x.std() #this is for calculating the standard deviation from the data


# In[24]:


x.count() #this is for calculating the counts of the days from the data


# In[25]:


x.describe() # this gives full description of the data in the data frame


# In[26]:


x.describe().transpose() # this gives full description of the data in the data frame showing the comparison


# In[ ]:




