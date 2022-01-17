#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]


# In[4]:


df = pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'],['W','X','Y','Z'])


# In[5]:


df


# In[17]:


df['P'] = df['Z']+df['Y'] #this is is a way of adding another column in data


# In[18]:


df


# In[20]:


df.drop('c') # this is for deleting a row


# In[21]:


df


# In[22]:


df.drop('P' , axis = 1 , inplace = True) #this is for deleting a column


# In[23]:


df


# In[24]:


df['Y'] # this is for accessing the columns


# In[25]:


df.loc['a'] # this is for accessing the rows


# In[26]:


df.iloc[1] # this is for accessing the rows


# In[27]:


df.loc['c','Z'] # this is for accessing a single element in the intersecting rows and columns in the data


# In[29]:


df[df > 3] #This is for accessing a set of values greaters than three in the table


# In[30]:


df[df["W"] > 3] #This is for accessing a set of values greaters than three in the table for a particular column


# In[31]:


df[df["W"] > 3][['W','X']] #This is for accessing a set of values greaters than three in the table for particular columns


# In[32]:


df[df["W"] > 3]['W'] #This is for accessing a set of values greaters than three in the table for particular columns


# In[33]:


df[df["W"] > 3][['W','X','Z']] #This is for accessing a set of values greaters than three in the table for particular columns


# In[34]:


df[(df["W"] > 3) & (df["Z"] > 5)] #This is for accessing a set of values using the conditional statement AND


# In[35]:


df[(df["W"] > 0) & (df["Z"] > 3)]


# In[36]:


df[(df["W"] > 0) | (df["Z"] > 3)]#This is for accessing a set of values using the conditional statement OR


# In[ ]:




