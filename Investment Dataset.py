#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


# Read the csv file
# Task 1: Data Overview
# Objective: Understand the dataset structure


# In[10]:


# Step 1: Load the dataset
data = pd.read_csv('Data_set 2 - Copy.csv')


# In[12]:


# Step 2: Descriptive Statistics - Used to gather information about the number of entries, columns, and data types.
data.info()


# In[13]:


# Task 1 successfully executed.


# In[14]:


# Task 2: Gender Distribution
# Objective: Visualize gender distribution in the dataset


# In[21]:


# Step 1: Extract Gender Information
gender = data['gender']


# In[20]:


# Step 2: Create a simple visualization chart, to represent the distribution of genders in the dataset with labels and count
gender_counts = gender.value_counts()
gender_counts.plot(kind='bar', title='Gender Distribution', color=['blue', 'pink'])
plt.xlabel('Gender')
plt.xticks(rotation=0)
plt.ylabel('Count')

for i, v in enumerate(gender_counts):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()


# In[26]:


# Task 2 succesfully executed.


# In[27]:


# Task 3: Descriptive Statistics
# Objective: Present basic statistics for numerical columns.


# In[28]:


# Step 1: Identify numerical columns in the dataset
numerical_columns = data.select_dtypes(include=['number']).columns
numerical_columns


# In[30]:


# Step 2: Use statistical functions to calculate the mean, median, and standard deviation for each numerical column.
numerical_stats = data[numerical_columns].agg(['mean', 'median', 'std'])
numerical_stats


# In[ ]:




