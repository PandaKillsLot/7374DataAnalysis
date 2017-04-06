
# coding: utf-8

# # Question I

# In[3]:

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[5]:

# relative path
vehicle_collisions = pd.read_csv('../Data/vehicle_collisions.csv')
vehicle_collisions.tail(5)


# In[7]:

df_NY = vehicle_collisions.loc[:,['DATE','BOROUGH']]
df_NY.tail()


# In[9]:

df = vehicle_collisions[vehicle_collisions.BOROUGH == 'MANHATTAN'].loc[:,['DATE','BOROUGH']]
df.head()


# In[10]:

# filter by year
def yyy(Series):
    return pd.to_datetime(Series).dt.year


# In[11]:

# filter by month
def mmm(Series):
    return pd.to_datetime(Series).dt.month


# In[12]:

df_2016 = df[yyy(df["DATE"]) == 2016]


# In[13]:

df_NY_2016 = df_NY[yyy(df_NY["DATE"]) == 2016]
df_NY_2016


# In[17]:

s_NYK = df_NY_2016.groupby(mmm(df_NY_2016.DATE)).count()['DATE']
s_NYK


# In[18]:

s_Man = df_2016.groupby(mmm(df_2016.DATE)).count()['DATE']
s_Man


# In[19]:

type(s_Man)


# In[20]:

S_index = pd.Series(["JAN","FEB","MAR","APR","MAY","JUNE","JULY","AUG","SEPT","OCT","NOV","DEC"])


# In[21]:

df_result = df2 = pd.DataFrame({
                                'MAN': s_Man,
                                'NYK': s_NYK,
                               })

df_result.index = S_index 

df_result


# In[22]:

df_result['Percentage'] = df_result['MAN']/df_result['NYK']
df_result


# In[23]:

df_result.to_csv('question1out.csv', encoding='utf-8')


# In[24]:

www = pd.read_csv('question1out.csv')
www.head()


# In[ ]:



