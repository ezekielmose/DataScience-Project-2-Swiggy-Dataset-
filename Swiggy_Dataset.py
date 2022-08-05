#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


swiggy_dataset=pd.read_csv("D:\Studies\Data Science\Projects\Project2\\Swiggy_50.csv")


# In[6]:


swiggy_dataset.head()


# In[9]:


swiggy_dataset.tail()


# In[12]:


swiggy_dataset["Cost for two"].mean()


# In[13]:


swiggy_dataset["Cost for two"].median()


# In[16]:


from statistics import variance


# In[18]:


variance(swiggy_dataset["Cost for two"])


# In[21]:


#weighted mean

import numpy as np
np.average(swiggy_dataset["Cost for two"], weights= swiggy_dataset ["Cost for two"])


# In[22]:


from statistics import stdev
stdev(swiggy_dataset["Cost for two"])


# In[25]:


q1= np.percentile (swiggy_dataset["Cost for two"], 75)
q1


# In[27]:


q2=np.percentile(swiggy_dataset["Cost for two"], 25)
q2


# In[29]:


q3=np.percentile(swiggy_dataset["Cost for two"], 50)
q3


# In[32]:


#mean absolute deviation

from numpy import mean, absolute


# In[35]:


mean(swiggy_dataset["Cost for two"]-mean(swiggy_dataset["Cost for two"]))


# In[38]:


#median absolute deviation
from numpy import median, absolute
median(swiggy_dataset["Cost for two"]-median(swiggy_dataset["Cost for two"]))


# In[43]:


#interquatile range

q3, q1=np.percentile(swiggy_dataset["Cost for two"],[75,25])
iqr=q3-q1
iqr


# In[46]:


import matplotlib.pyplot as plt


# In[59]:


#histogram
plt.hist(x=swiggy_dataset["Cost for two"], bins=10, color='#0504aa', alpha=1, rwidth=0.9)


# In[61]:


#boxplot

swiggy_dataset.boxplot(column="Cost for two", by=None, ax= None)


# In[81]:


#density plot
ax= swiggy_dataset["Cost for two"].plot.hist(density=True, xlim=[5,100],bins=range (5,100), rwidth=0.9, color='#0504aa', alpha=1)
swiggy_dataset["Cost for two"].plot.density(ax=ax)


# In[ ]:





# In[ ]:




