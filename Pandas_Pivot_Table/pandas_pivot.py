#!/usr/bin/env python
# coding: utf-8

# ## Pandas Pivot Table

# #### 1.	Write a Python script to sort (ascending and descending) a dictionary by value..

# In[9]:


d={'a':10,'b':20,'c':30,'d':4,'e':5,'f':6}


d_asc=dict(sorted(d.items(), key=lambda x: x[1], reverse=False))
print('Asecding order dictionary:', d_asc)

d_desc=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print('Descending order dictionary:', d_desc)


# #### 2.	Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise

# In[10]:


import numpy as np
import pandas as pd


# In[11]:


df=pd.read_excel("Sales_data_Panda_numpy.xlsx")
df.head()


# In[12]:


df=pd.read_excel("Sales_data_Panda_numpy.xlsx",thousands=',')
df.head()


# In[ ]:





# In[13]:


df.pivot_table(values='Sale_amt',index='Region',columns='Manager',margins=True,aggfunc='sum')


# #### 3.	Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.

# In[14]:


df.pivot_table(values='Sale_amt',index='Region',columns=['Manager','SalesMan'],margins=True,aggfunc='sum')


# In[15]:


df.pivot_table(values='Sale_amt',index=['Region','Manager','SalesMan'],margins=True,aggfunc='sum')


# #### 4.	Write a Pandas program to create a Pivot table and find the item wise unit sold.

# In[16]:


df.pivot_table(values='Units',index='Item',margins=True,aggfunc='sum')


# #### 5.	Write a Pandas program to create a Pivot table and find the region wise total sale.

# In[17]:


df.pivot_table(values='Sale_amt',index='Region',margins=True,aggfunc='sum')


# #### 6.	Write a Pandas program to create a Pivot table and find the region wise, item wise unit sold.

# In[18]:


df.pivot_table(values='Units',index='Region',columns='Item',margins=True,aggfunc='sum')


# #### 7.	Write a Pandas program to create a Pivot table and count the manager wise sale and mean value of sale amount. 

# In[19]:


df.pivot_table(values='Sale_amt',index='Manager',margins=True,aggfunc=['count','mean'])


# #### 8.	Write a Pandas program to create a Pivot table and find manager wise, salesman wise total sale and also display the sum of all sale amount at the bottom. 

# In[20]:


df.pivot_table(values=['Sale_amt','Units'],index=['Manager','SalesMan'],margins=True,aggfunc='sum')


# #### 9.	 Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise where Manager = "Douglas".

# In[21]:


table=df.pivot_table(values='Sale_amt',index=['Region','Manager','SalesMan'],margins=True,aggfunc='sum')

table.query('Manager == "Douglas"')


# #### 10.	Write a Pandas program to create a Pivot table and find the region wise Television and Home Theater sold.

# In[22]:


table=df.pivot_table(values='Units',index=['Region','Item'],margins=True,aggfunc='sum')
table.query('Item==["Television","Home Theater"]')


# In[ ]:





# In[ ]:




