
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[2]:

employee_compensation = pd.read_csv('../Data/employee_compensation.csv')


# In[3]:

employee_compensation.head()


# In[4]:

df = employee_compensation[employee_compensation['Year Type'] == 'Calendar']
df


# In[5]:

df.shape


# In[6]:

df['Job Family'].unique().size


# In[7]:

#df['Job Family Code'].apply(lambda x : int(x) if x.isdigit() else 1111111)
# lambda x : int(x[-5:-1]) if x[-5 : -1].isdigit() else 1990


# In[8]:

s = df.groupby('Employee Identifier').mean()
s
#.loc[:,['Salaries', 'Overtime', 'Other Salaries', 'Total Salary','Retirement','Other Benefits','Total Benefits','Total Compensation']]


# In[9]:

df1 = s[s.Overtime > s.Salaries * 0.1]
df1


# In[10]:

l = list(df1.index)
l[0:10]


# In[11]:

df = df[df['Employee Identifier'].isin(l)]
df


# In[12]:

df.shape


# In[13]:

df = df.loc[:,['Job Family', 'Total Benefits', 'Total Compensation']]
df


# In[14]:

df.shape


# In[15]:

df_result = df.groupby('Job Family').mean()


# In[16]:

df_result.head()


# In[17]:

df_result.index.size


# In[18]:

df_result['Percent_Total_Benefit'] = df_result['Total Benefits'] / df_result['Total Compensation'] * 100


# In[19]:

df_result


# In[20]:

df_result.to_csv('question22out.csv', encoding='utf-8')
www = pd.read_csv('question22out.csv')
www.head()


# In[ ]:




# In[ ]:



