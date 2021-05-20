#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Terrorism

# # The Sparks Foundation

# In[1]:


#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl


# In[2]:


df = pd.read_csv(r"globalterrorismdb_0718dist.csv",encoding='latin1')
df.head() # read data


# In[3]:


df.shape


# In[4]:


df.tail(1)


# In[5]:


df.keys().values


# In[9]:


df.info()


# In[6]:


#check missing value
df.isnull().sum()


# In[8]:


(181691*60)/100


# # data cleaning

# In[13]:


for i in df.columns:
    a=df[i]
    b=a.isnull().sum()
    if b > 109014.6:
        df.drop([i],axis=1,inplace=True)
print(df.columns.values)


# In[14]:


df.head().T


# # 10 countries with highest amount of attacks

# In[17]:


plt.figure(figsize=(9,9))
a=df['country_txt'].value_counts().reset_index()
a.columns=['country','attacks']
a=a.head(10)
sns.barplot(a['country'],a['attacks'])
plt.xticks(rotation=90)
plt.show()


# # year with highest amount of attacks

# In[18]:


a=df['iyear'].value_counts().reset_index()
a.columns=['year','attacks']
plt.figure(figsize=(10,5))
sns.barplot(a['year'],a['attacks'])
plt.xticks(rotation=90)
plt.show()


# # attack type at year 2014 in Iraq

# In[19]:


a=df['iyear']==2014
b=df['country_txt']=='Iraq'
c=a&b
d=df['attacktype1_txt']
e=d[c]
sns.countplot(e)
plt.xticks(rotation=90)
plt.show()


# In[26]:


a=df['iyear']==2014
b=df['country_txt']=='Iraq'
c=a&b
d=df['city']
e=d[c].value_counts().head(20)
f=e.index
g=e.values
h=pd.DataFrame({'city':f,'incidents':g})
plt.figure(figsize=(15,5))
sns.barplot(h['city'],h['incidents'])
plt.xticks(rotation=90)
plt.show()


# # their target

# In[27]:


a=df['iyear']==2014
b=df['country_txt']=='Iraq'
c=a&b
d=df['targtype1_txt']
e=d[c]
sns.countplot(e)
plt.xticks(rotation=90)
plt.show()


# # wepons uesed on target type :- Private citizens and Property

# In[28]:


a=df['iyear']==2014
b=df['country_txt']=='Iraq'
c=a&b
d=df['targtype1_txt']=='Private Citizens & Property'
e=c&d
f=df['weaptype1_txt']
g=f[e]
sns.countplot(g)
plt.xticks(rotation=90)
plt.show()


# In[ ]:




