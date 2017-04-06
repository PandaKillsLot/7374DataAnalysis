
# coding: utf-8

# # Question 3 

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[3]:

# read and glance
cricket_matches = pd.read_csv('../Data/cricket_matches.csv')
cricket_matches.tail()


# In[4]:

# filter those team wins at home
df = cricket_matches[cricket_matches['home'] == cricket_matches['winner']]
df.head()


# In[11]:

# only left useful cols
df_filter = df.loc[:,['winner','innings1','innings1_runs','innings2','innings2_runs']]
df_filter


# In[12]:

#df_filter['innings1_runs'] = df_filter['innings2_runs']


# In[13]:

# teams win in the first innings
df_1 = df_filter[df_filter.winner == df_filter.innings1]
df_1.shape


# In[14]:

# teams win in the first innings
df_2 = df_filter[df_filter.winner == df_filter.innings2]
df_2.shape


# In[15]:

# group by team  and add up
a = df_1.groupby('winner').sum()
a = a.innings1_runs
a


# In[16]:

b = df_2.groupby('winner').sum()
b = b.innings2_runs
b


# In[17]:

# add up all winned points
c = a.add(b, fill_value=0)
c


# In[18]:

df_result = df_filter.groupby('winner').mean()
df_result


# In[19]:

# count how many times they won
df3 = df_filter.groupby('winner').count()


# In[20]:

df3


# In[22]:

# new col
df3['totalSum'] = c


# In[23]:

df3.head()


# In[24]:

# total points / times
df3['Score'] = df3.totalSum / df3.innings1


# In[25]:

df3


# In[26]:

aaa = df3.loc[:,['Score']]


# In[27]:

aaa


# In[62]:

aaa.index.name = 'home'
aaa


# In[28]:

# output


# In[30]:

aaa.to_csv('question3out.csv', encoding='utf-8')
www = pd.read_csv('question3out.csv')
www.head()


# In[ ]:



