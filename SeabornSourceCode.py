#!/usr/bin/env python
# coding: utf-8

# # Installation

# In[1]:


pip install seaborn


# # Import library

# In[2]:


import pandas as pd #working on data frames
import numpy as np #numerical
import seaborn as sns #using library
import matplotlib.pyplot as plt #using library
import time #calculate the time
from time import process_time


# # Import Data

# In[3]:


data = pd.read_csv('../heart_disease.csv') #open file import data


# In[4]:


data


# # Data analysis

# #### Step1: Understanding the data

# In[5]:


data.head() #To show first five rows


# In[6]:


data.tail() #To show last five rows


# In[7]:


data.shape #Total column that is contained Dataset (303 rows, 14 columns)


# In[8]:


data.describe() #Summary descriptive statistics based solely on numerical numbers


# In[9]:


data.columns #To check all columns in the file


# In[10]:


data.nunique()


# In[11]:


data.dtypes


# In[12]:


data['age'].unique()


# In[13]:


data['sex'].unique()


# In[14]:


data['cp'].unique()


# In[15]:


data['trestbps'].unique()


# In[16]:


data['chol'].unique()


# In[17]:


data['fbs'].unique()


# In[18]:


data['restecg'].unique()


# In[19]:


data['thalach'].unique()


# In[20]:


data['exang'].unique()


# In[21]:


data['oldpeak'].unique()


# In[22]:


data['ca'].unique()


# In[23]:


data['thal'].unique()


# In[24]:


data['target'].unique()


# #### Step 2: Cleaning Data

# In[25]:


data.isnull().sum ()


# #### Step 3: Analysing Data

# Here, we will use a heatmap to have an overview relationships between data

# In[26]:


# creating a colormap
colormap = sns.color_palette('Blues')
#creating a heatmap
fig,ax=plt.subplots(figsize=(16,16))
correlation=data.corr()
sns.heatmap(correlation,xticklabels=correlation.columns,yticklabels=correlation.columns,annot=True,cmap=colormap)
#set title of graph
plt.title('Heatmap for Heart Disease Data Sheet')


# #### Filtering data

# In[27]:


#We divide cholesterol into 5 different ranges
bins=[100,200,300,400,500,600]
data['grouped_chol'] = pd.cut(data['chol'], bins=bins) 


# In[28]:


print(data['grouped_chol'])


# In[29]:


#We divide age into 6 different ranges
bins=[20,30,40,50,60,70,80]
data['grouped_age'] = pd.cut(data['age'], bins=bins) 


# In[30]:


print(data['grouped_age'])


# In[31]:


#We divide oldpeak into 6 different ranges
bins=[0,1,2,3,4,5,6,7]
data['grouped_oldpeak'] = pd.cut(data['oldpeak'], bins=bins) 


# In[32]:


print(data['grouped_oldpeak'])


# #### Setting color palette and style for Seaborn graphs

# In[33]:


sns.set_palette('prism')  #set colorpalette
sns.set_style('whitegrid') #set graph style


# ##### Start plotting

# This is used to count for time taken to generate a graph which will be used in the library comparison in our report

# In[34]:


#Start the stopwatch/counter
t1_start = process_time()

fig,ax=plt.subplots(figsize=(7,6))
x=data['age']
sns.histplot(x=x,bins=6).set(title='Histogram of Age')

#Stop the stopwatch / counter
t1_stop = process_time()
print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)


# In[35]:


fig,ax=plt.subplots(figsize=(7,6)) #setting figure's size
x=data['grouped_age']
sns.countplot(x=x,hue=data['target'])
plt.title('Column graph for Age') #setting graph's title


# In[36]:


fig,ax=plt.subplots(figsize=(7,6))
sns.kdeplot(data['age'],hue=data['target'],shade=True,thresh=0,multiple='stack')
plt.title('KDE for Age')


# In[37]:


fig,ax=plt.subplots(figsize=(7,6))
x=data['grouped_chol']
hue=data['target']
sns.countplot(x=x,hue=hue)
plt.title('Column graph for Chol')


# In[38]:


fig,ax=plt.subplots(figsize=(8,6))
sns.swarmplot(x='age',y='grouped_chol',data=data,size=4,hue='target')
plt.title('Scatter Plot for Age against Chol')


# In[39]:


fig,ax=plt.subplots(figsize=(10,6))
sns.lineplot(y='chol',x='age',data=data,hue="target",style='target',markers=True, dashes=False,err_style="bars", ci=68)
plt.title('Line Plot for Age against Chol')


# In[40]:


fig,ax=plt.subplots(figsize=(9,6))
sns.boxplot(x='grouped_age',y='chol',data=data,palette='bright')
plt.title('Box Plot for Age against Chol')


# In[60]:


jp=sns.jointplot(x='age',y='chol',data=data)
jp.set_axis_labels(xlabel='age',ylabel='chol')#setting x and y-axis labels
jp.fig.suptitle('Joint Plot for age against chol',fontsize=11) #setting graph's title


# In[41]:


fig,ax=plt.subplots(figsize=(7,6))
sns.stripplot(x='exang',y='age',data=data,hue='target')
plt.title('Scatter Plot for Exang against Age')


# In[42]:


fig,ax=plt.subplots(figsize=(7,6))
sns.countplot(data=data,x='slope',hue='target')
plt.title('Column graph for Slope')


# In[43]:


fig,ax=plt.subplots(figsize=(10,6))
sns.stripplot(x='grouped_oldpeak',y='age',data=data,hue='target')
plt.title('Scatter Plot for Oldpeak against Age')


# In[44]:


fig,ax=plt.subplots(figsize=(10,6))
sns.boxplot(x='grouped_oldpeak',y='age',data=data,hue='target')
plt.title('Box Plot for Oldpeak against Age')


# In[45]:


fig,ax=plt.subplots(figsize=(7,6))
x=data['oldpeak']
hue=data['target']
sns.kdeplot(x=x,hue=hue,shade=True,multiple='stack')
plt.title('KDE graph for Oldpeak')


# In[46]:


fig,ax=plt.subplots(figsize=(7,6))
sns.boxenplot(x='sex',y='age',data=data,hue="target")
plt.title('Boxen Plot for Sex')


# In[47]:


fig,ax=plt.subplots(figsize=(7,6))
sns.kdeplot(data['sex'],hue=data['target'],shade=True)
plt.title('KDE graph for Sex')


# In[48]:


fig,ax=plt.subplots(figsize=(12,4))
sns.pointplot(x='age',y='fbs',data=data,hue='target',ci='sd',join=False)
plt.title('Point Plot for Age against Ca')


# In[49]:


fig,ax=plt.subplots(figsize=(12,4))
sns.pointplot(x='grouped_age',y='restecg',data=data,hue='target',ci='sd',join=True)
plt.title('Point Plot for Age against Ca')

