#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[18]:


import pandas as pd


# In[19]:


x1 = {'a':[1,1,1,1,1],'b':[1,1,1,1,1],'c':[1,1,1,1,1],'d':[1,1,1,1,1],'e':[1,1,1,1,1]}
x2 = {'e':[2,2,2,2,2],'f':[2,2,2,2,2],'g':[2,2,2,2,2],'h':[2,2,2,2,2],'i':[2,2,2,2,2]}
x3 = {'a':[3,3,3,3,3],'b':[3,3,3,3,3],'c':[3,3,3,3,3],'d':[3,3,3,3,3],'e':[3,3,3,3,3]}


# In[20]:


df1 = pd.DataFrame(x1 , index = [1,2,3,4,5])
df2 = pd.DataFrame(x2 , index = [1,2,3,4,5])
df3 = pd.DataFrame(x3 , index = [1,2,3,4,5])


# In[21]:


df1


# In[22]:


pd.concat([df1,df2])


# In[23]:


pd.concat([df1,df3])


# In[24]:


pd.concat([df1,df3], axis = 1)


# In[25]:


pd.concat([df1,df2,df3])


# In[27]:


pd.concat([df1,df2,df3], axis = 1 )


# In[ ]:




