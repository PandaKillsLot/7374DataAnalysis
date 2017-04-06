
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[2]:

# relative path
employee_compensation = pd.read_csv('../Data/employee_compensation.csv')


# In[3]:

employee_compensation.tail(30)


# In[4]:

df = employee_compensation.loc[:,['Organization Group','Department','Total Compensation']]
df.head()
#s.groupby(level=['first', 'second']).sum()
#df['C'].groupby(df['A'])


# In[7]:

df_sorted = df.sort_values(by='Organization Group')


# In[8]:

df_sorted.head()


# In[11]:

df_results = df_sorted.groupby(["Organization Group","Department"]).mean()


# In[12]:

df_results.to_csv('question21out.csv', encoding='utf-8')
www = pd.read_csv('question21out.csv')
www.head()


# In[ ]:



