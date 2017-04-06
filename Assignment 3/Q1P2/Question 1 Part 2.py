
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[3]:

# relative path
vehicle_collisions = pd.read_csv('../Data/vehicle_collisions.csv')
vehicle_collisions.tail(5)


# In[4]:

df =vehicle_collisions.loc[:,['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE', 'VEHICLE 5 TYPE']]
df


# In[5]:

s = df.groupby("BOROUGH").count()
s


# In[6]:

df_results = s.copy()
df_results


# In[7]:

df_results["VEHICLE 3 TYPE"] = s["VEHICLE 3 TYPE"] - s["VEHICLE 4 TYPE"]
df_results["VEHICLE 2 TYPE"] = s["VEHICLE 2 TYPE"] - s["VEHICLE 3 TYPE"]
df_results["VEHICLE 1 TYPE"] = s["VEHICLE 1 TYPE"] - s["VEHICLE 2 TYPE"] 


# In[8]:

df_results


# In[9]:

df_results.to_csv('question12out.csv', encoding='utf-8')
www = pd.read_csv('question12out.csv')
www.head()


# In[ ]:



