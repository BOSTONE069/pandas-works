#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


x1 = {'a':[1,2,3],'b':[5,6,7]}
x2 = {'c':[3,4,5],'d':[2,3,6]}


# In[8]:


x = pd.DataFrame(x1 , index = ['p1','p2','p3'])
y = pd.DataFrame(y1 , index = ['p1','p2','p3'])


# In[9]:


x


# In[10]:


y


# In[11]:


x.join(y) #this is for joining the data sets


# In[ ]:




