#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the necessary libraries
import numpy as np
import pandas as pd
from scipy.stats import stats


# In[2]:


df = pd.read_csv("C:/Users/George/Downloads/01.Data Cleaning and Preprocessing.csv")


# In[3]:


print(df.info)


# In[4]:


type(df)


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.describe()


# In[8]:


df.shape


# In[9]:


df.isnull()


# In[10]:


df.isnull().sum()


# In[11]:


df.isnull().sum().sum()


# In[12]:


df.notnull()


# In[13]:


df_cleaned = df.dropna()
df_cleaned


# In[14]:


print(df_cleaned.head())


# In[15]:


df_filled = df.fillna(value=0)
df_filled


# In[16]:


df.fillna(method="pad")
df


# In[17]:


df.fillna(method="ffill")
df


# In[18]:


df.fillna(method="bfill")
df


# In[19]:


df.columns


# In[20]:


print(df_filled.head())


# In[21]:


df_no_duplicates = df.drop_duplicates()
df_no_duplicates


# In[22]:


print(df_no_duplicates.head())


# In[23]:


filtered_data = df[df["BlowFlow"]>16]
filtered_data


# In[24]:


print(filtered_data.head())


# In[25]:


sorted_data = df.sort_values(by='ChipRate', ascending=True)
sorted_data


# In[26]:


print(sorted_data.head())


# In[27]:


grouped_data = df.groupby('ChipMass-4 ').sum() 
grouped_data


# In[28]:


print(grouped_data.head())

