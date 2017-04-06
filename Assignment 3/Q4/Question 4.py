
# coding: utf-8

# # Question 4

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[3]:

# read the csv
movies_awards = pd.read_csv('../Data/movies_awards.csv')
movies_awards.head(3)


# In[185]:

# only keep selected columns
df = movies_awards.loc[:,['Title','Awards']]


# In[186]:

# show
df.head(3)


# In[187]:

# convert the type for further operatin
df['Awards'] = df['Awards'].astype('str') 
df


# In[188]:

# check the value form
df['Awards'][df.Title == 'Seabiscuit'].values[0]


# In[241]:

# a glance into the form of 'award' col
df['Awards'].unique()[0:50]


# In[190]:

# use regex
import re


# # wins & nominations

# In[191]:

# sample test
g = '3 wins & 5 nominations'
# pattern
pattern_win = re.compile(r'(\d) win')
# check whether matches
match = pattern_win.match(g)
print(match)
if match:
    print("1111")
#check the value form

print(match.group().split(' ')[0])


# In[192]:

# apply the regex and split a new col from the old
df['Award_wins'] = df['Awards'].apply(lambda x: pattern_win.match(x).group().split(' ')[0] if pattern_win.match(x) else 0)


# In[193]:

#check
df.head(6)


# In[194]:

# check the data
df['Award_wins'].unique()


# In[195]:

g = '3 wins & 5 nominations'
pattern_nominations = re.compile(r'\b(\d)\b.*\bnominations\b')
match = pattern_nominations.match(g)
print(match)
if match:
    print("1111")
print(match.group().split(' ')[-2])


# In[196]:

df['Award_nominated'] = df['Awards'].apply(lambda x: pattern_nominations.match(x).group().split(' ')[-2] if pattern_nominations.match(x) else 0)


# In[197]:

df.head(7)


# In[198]:

df['Award_nominated'].unique()


# # Oscar Nominated & Won

# In[199]:

pattern_oscar_nominated = re.compile(r'Nominated for (\d) Oscars')


# In[242]:

s = 'Nominated for 7 Oscars'
match = pattern_oscar_nominated .match(s)
print(match)
if match:
    print("1111")


# In[201]:

match.group().split(' ')[2]


# In[202]:

df['oscar_nominated'] = df['Awards'].apply(lambda x: pattern_oscar_nominated .match(x).group().split(' ')[2] if pattern_oscar_nominated .match(x) else 0)


# In[203]:

df.head()


# In[204]:

df['oscar_nominated'].unique()


# In[205]:

g = 'Won 3 Oscars'
pattern_oscar_won = re.compile(r'Won (\d) Oscars')
match = pattern_oscar_won.match(g)
print(match)
if match:
    print("1111")
print(match.group().split(' ')[1])


# In[206]:

df['Oscar_Won'] = df['Awards'].apply(lambda x: pattern_oscar_won.match(x).group().split(' ')[1] if pattern_oscar_won.match(x) else 0)
df.head()


# In[207]:

df['Oscar_Won'].unique()


# # Golden glob nominated & won

# In[208]:

g = 'Nominated for 1 Golden Globe'


# In[209]:

pattern_Golden_nominated = re.compile(r'Nominated for (\d) Golden Globe')


# In[210]:

match = pattern_Golden_nominated.match(g)
print(match)
if match:
    print("1111")


# In[211]:

match.group().split(' ')[2]


# In[212]:

df['Golden_Globe_nominated'] = df['Awards'].apply(lambda x: pattern_Golden_nominated .match(x).group().split(' ')[2] if pattern_Golden_nominated .match(x) else 0)


# In[213]:

df.head()


# In[214]:

df['Golden_Globe_nominated'].unique()


# In[215]:

g = 'Won 1 Golden Globe'
pattern_golden_won = re.compile(r'Won (\d) Golden Globe')
match = pattern_golden_won.match(g)
print(match)
if match:
    print("1111")
print(match.group().split(' ')[1])


# In[216]:

df['Golden_Globe_Won'] = df['Awards'].apply(lambda x: pattern_golden_won.match(x).group().split(' ')[1] if pattern_golden_won.match(x) else 0)
df.head()


# In[217]:

df['Golden_Globe_Won'].unique()


# # Primetime Emmy nominated and won

# In[218]:

g = 'Nominated for 1 Primetime Emmy'
pattern_Primetime_nominated = re.compile(r'Nominated for (\d) Primetime Emmy')
match = pattern_Primetime_nominated.match(g)
print(match)
if match:
    print("1111")


# In[219]:

match.group().split(' ')[2]


# In[220]:

df['Primetime_Emmy_nominated'] = df['Awards'].apply(lambda x: pattern_Primetime_nominated .match(x).group().split(' ')[2] if pattern_Primetime_nominated .match(x) else 0)


# In[221]:

df.head()


# In[222]:

df['Primetime_Emmy_nominated'].unique()


# In[223]:

g = 'Won 3 Primetime Emmys'
pattern_Primetime_won = re.compile(r'Won (\d) Primetime Emmys')
match = pattern_Primetime_won.match(g)
print(match)
if match:
    print("1111")
print(match.group().split(' ')[1])


# In[224]:

df['Primetime_Emmys_Won'] = df['Awards'].apply(lambda x: pattern_Primetime_won.match(x).group().split(' ')[1] if pattern_Primetime_won.match(x) else 0)
df.head()


# In[225]:

df['Primetime_Emmys_Won'].unique()


# # BAFTA nominated and won

# In[226]:

g = 'Nominated for 1 BAFTA Film Award'
pattern_BAFTA_nominated = re.compile(r'Nominated for (\d) BAFTA Film Award')
match = pattern_BAFTA_nominated.match(g)
print(match)
if match:
    print("1111")
print(match.group().split(' ')[2])


# In[227]:

df['BAFTA_Film_nominated'] = df['Awards'].apply(lambda x: pattern_BAFTA_nominated.match(x).group().split(' ')[2] if pattern_BAFTA_nominated.match(x) else 0)


# In[228]:

df.head()


# In[229]:

df['BAFTA_Film_nominated'].unique()


# In[230]:

g = 'Won 3 BAFTA Film Award'
pattern_BAFTA_won = re.compile(r'Won (\d) BAFTA Film Award')
match = pattern_BAFTA_won.match(g)
print(match)
if match:
    print("1111")
print(match.group().split(' ')[1])


# In[231]:

df['BAFTA_Film_won'] = df['Awards'].apply(lambda x: pattern_BAFTA_won.match(x).group().split(' ')[2] if pattern_BAFTA_won.match(x) else 0)


# In[232]:

df.head()


# In[233]:

df['BAFTA_Film_won'].unique()


# # save to csv

# In[237]:

df.to_csv('question4out.csv', encoding='utf-8')


# In[239]:

www = pd.read_csv('question4out.csv')


# In[240]:

www.head()


# In[ ]:




# In[ ]:



