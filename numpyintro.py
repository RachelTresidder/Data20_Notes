#!/usr/bin/env python
# coding: utf-8

# # Numpy Intro

# In[1]:


import numpy as np


# In[2]:


list1 = [10, 20, 30]
list1


# In[3]:


arr1 = np.array(list1)
arr1


# In[5]:


type(list1)


# In[6]:


type(arr1)


# In[26]:


arr2 = np.arange(10,21, 1)
arr2


# In[11]:


list2 = [40, 30, 50]
list3 = [list1, list2]


# In[12]:


arr3 = np.array(list3)
arr3


# In[13]:


type(arr3)


# In[14]:


arr3.shape


# In[16]:


arr3dim = np.array([[[1, 2, 3],[4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])
arr3dim


# In[17]:


arr3dim.shape


# In[18]:


list1 * 3


# In[20]:


arr3dim * 3


# In[24]:


arr2 = np.array(list2)
arr2


# In[23]:


arr1*arr2


# In[25]:


arr1*arr3dim


# In[27]:


arr1 * arr2


# In[31]:


arr1d = np.arange(1, 13, 1)
arr1d.shape


# In[41]:


arr2d_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
arr2d = np.array(arr2d_list)
arr2d.shape


# In[42]:


arr3d_list = [[[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]], [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]]
arr3d = np.array(arr3d_list)
arr3d.shape


# In[43]:


arr3


# In[44]:


arr3[1][2]


# In[45]:


arr3[0]


# In[46]:


arr3[1][2]*2


# In[47]:


arr3[0:2][1:2]


# In[48]:


arr3[::2][1:2]


# In[50]:


arr3[:,2]


# In[54]:


arr3.sum()
arr3


# In[55]:


arr3.mean()
arr3


# In[56]:


for x in arr3:
    print(x)


# In[62]:


for x in arr3:
    for num in x:
        print(num)


# In[64]:


for x in np.nditer(arr3):
    print(x)


# In[ ]:




