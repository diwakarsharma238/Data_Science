#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[142]:


df=pd.read_csv('company_sales_data (1).csv',index_col=0)


# In[143]:


df


# ## Line Chart

# In[41]:


fig=plt.figure()

ax=fig.add_axes([0,0,1,1])
ax.plot(df['facecream'],label='Facecream')
ax.plot(df['facewash'],label='FaceWash')
ax.plot(df['toothpaste'],label='ToothPaste')
ax.plot(df['bathingsoap'],label='BathingSoap')
ax.plot(df['shampoo'],label='Shampoo')
ax.plot(df['moisturizer'],label='Moisturizer')

ax.set_xlabel('Month Number')
ax.set_ylabel('Moththly Sale (units)')
ax.set_title('Monthly Sale (Units)')

ax.legend()


# ## Pie Chart

# In[44]:


df_sum=df.sum()


# In[58]:


sales_sum=df_sum.iloc[[0,1,2,3,4,5]]


# In[70]:


sales_sum


# In[74]:


sales_sum.values


# In[76]:


sales_sum.index


# In[96]:


plt.pie(sales_sum.values,labels=sales_sum.index, autopct='%1.1f%%')
plt.title('Totale Sale Share')
plt.show()


# 
# ## Bar Chart

# In[104]:


plt.bar(df.index,df['total_profit'])
plt.title('Monthly Total sale')
plt.xlabel('Month')
plt.ylabel('Monthly sale (units)')
plt.show()


# ## Histogram

# In[138]:


fig, axes = plt.subplots(2, 3, figsize=(16,10))

axes[0][0].hist(df['facecream'],bins=5)
axes[0][0].set_xlabel('sales(units)')
axes[0][0].set_ylabel('Frequency')
axes[0][0].set_title('Monthly sales - Facecream')

axes[0][1].hist(df['facewash'],bins=5)
axes[0][1].set_xlabel('sales(units)')
axes[0][1].set_ylabel('Frequency')
axes[0][1].set_title('Monthly sales - FaceWash')

axes[0][2].hist(df['toothpaste'],bins=5)
axes[0][2].set_xlabel('sales(units)')
axes[0][2].set_ylabel('Frequency')
axes[0][2].set_title('Monthly sales - Toothpaste')

axes[1][0].hist(df['bathingsoap'],bins=5)
axes[1][0].set_xlabel('sales(units)')
axes[1][0].set_ylabel('Frequency')
axes[1][0].set_title('Monthly sales - BathingSoap')

axes[1][1].hist(df['shampoo'],bins=5)
axes[1][1].set_xlabel('sales(units)')
axes[1][1].set_ylabel('Frequency')
axes[1][1].set_title('Monthly sales - Shampoo')

axes[1][2].hist(df['moisturizer'],bins=5)
axes[1][2].set_xlabel('sales(units)')
axes[1][2].set_ylabel('Frequency')
axes[1][2].set_title('Monthly sales - Moisturizer')


plt.show()


# In[ ]:




