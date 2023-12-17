#!/usr/bin/env python
# coding: utf-8

# # Installation

# In[1]:


pip install matplotlib


# # Import library

# In[2]:


import pandas as pd #working on data frames
import numpy as np #numerical
import matplotlib.pyplot as plt #using library
import time #calculate the time
from time import process_time


# # Import Data 

# In[3]:


data = pd.read_csv('C:/Users/behji/Downloads/heart_disease.csv.csv') #open file import data


# In[4]:


data


# # Data analysis

# Step1: Understanding the data

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


#A dtype='object' (an instance of the numpy. dtype class) specifies how bytes in the fixed-size memory block 
#corresponding to an array item should be interpreted.


# In[11]:


data.nunique()


# In[12]:


# dtype: int64 which means each value in this column is stored as a 64-bit integer in Python


# In[13]:


data.dtypes


# In[14]:


data['age'].unique()


# In[15]:


data['sex'].unique()


# In[16]:


data['cp'].unique()


# In[17]:


data['trestbps'].unique()


# In[18]:


data['chol'].unique()


# In[19]:


data['fbs'].unique()


# In[20]:


data['restecg'].unique()


# In[21]:


data['thalach'].unique()


# In[22]:


data['exang'].unique()


# In[23]:


data['oldpeak'].unique()


# In[24]:


data['slope'].unique()


# In[25]:


data['ca'].unique()


# In[26]:


data['thal'].unique()


# In[27]:


data['target'].unique()


# Step 2: Cleaning Data

# In[28]:


data.isnull().sum ()


# Step 3: Analysing Data

# Graph: Age Distribution

# In[29]:


#Start the stopwatch/counter
t1_start = process_time()

plt.hist(data['age'],color='maroon')
plt.xlabel('age')
plt.title('Distribution of Age')
plt.show()

#Stop the stopwatch / counter
t1_stop = process_time()
print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)


# Graph: Age vs Chol vs Target

# In[30]:


x=data['chol']
y=data['age']
z=data['target']
plt.xlabel('Chol & Target')
plt.ylabel('Age')
plt.title('Age against Chol & Target')
plt.scatter(x,y,label='chol')
plt.scatter(z,y,label='target')
plt.legend(loc='upper right')
plt.scatter(x,y)
plt.show()


# Graph: Number of Sex

# In[31]:


data['sex'].value_counts().plot(kind='bar')
plt.title('Number of sex')
plt.xlabel('sex')
plt.ylabel('total')
plt.show()


# Graph: Target vs Sex

# In[32]:


pclass_xt = pd.crosstab(data['target'], data['sex'])
pclass_xt.astype('int64')


# In[33]:


pclass_xt = pd.crosstab(data["sex"], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against sex')
plt.legend()
plt.show()


# Graph: Pie chart of cp

# In[34]:


x = list(data['cp'].value_counts())
labels = list(data['cp'].value_counts().index)
plt.subplots(figsize=(10,6),dpi=70)
colors = ['y','r','orange','yellow']
plt.pie(x,labels=labels,colors=colors, autopct = '%1.1f%%', startangle=90) 
plt.title("cp",fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.axis('equal')
plt.show()


# Graph: Number of cp

# In[35]:


data['cp'].value_counts().plot(kind='bar')
plt.title('Number of cp')
plt.xlabel('cp')
plt.ylabel('total')
plt.show()


# Graph: Target vs cp

# In[36]:


pclass_xt = pd.crosstab(data['target'], data['cp'])
pclass_xt.astype('int64')


# In[37]:


pclass_xt = pd.crosstab(data["cp"], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against cp')
plt.legend()
plt.show()


# Graph: Target vs Chol

# In[38]:


x=data['chol']
y=data['target']
plt.figure(figsize=(20,5))
plt.scatter(x,y,color='orange')
plt.title('Target against Chol')
plt.xlabel('chol')
plt.ylabel('target')
plt.show()


# Graph: Pie chart of fbs

# In[39]:


x = list(data['fbs'].value_counts())
labels = list(data['fbs'].value_counts().index)
plt.subplots(figsize=(10,6),dpi=70)
colors = ['violet','lavender']
plt.pie(x,labels=labels,colors=colors, autopct = '%1.1f%%', startangle=90) 
plt.title("fbs",fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.axis('equal')
plt.show()


# Graph: Target vs fbs

# In[40]:


pclass_xt = pd.crosstab(data['target'], data['fbs'])
pclass_xt.astype('int64')


# In[41]:


pclass_xt = pd.crosstab(data["fbs"], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against fbs')
plt.legend()
plt.show()


# Graph: Pie chart of restecg

# In[42]:


x = list(data['restecg'].value_counts())
labels = list(data['restecg'].value_counts().index)
plt.subplots(figsize=(10,6),dpi=70)
colors = ['gold','silver','purple']
plt.pie(x,labels=labels,colors=colors, autopct = '%1.1f%%', startangle=90) 
plt.title("restecg",fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.axis('equal')
plt.show()


# Graph: Target vs restecg

# In[43]:


pclass_xt = pd.crosstab(data['target'], data['restecg'])
pclass_xt.astype('int64')


# In[44]:


pclass_xt = pd.crosstab(data["restecg"], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against restecg')
plt.legend()
plt.show()


# Graph: Target vs Thalach

# In[45]:


x=data['thalach']
y=data['target']
plt.figure(figsize=(14,5))
plt.scatter(x,y,color='green')
plt.title('Target against Thalach')
plt.xlabel('thalach')
plt.ylabel('target')
plt.show()


# Graph: Pie chart of exang

# In[46]:


x = list(data['exang'].value_counts())
labels = list(data['exang'].value_counts().index)
fig,ax=plt.subplots(figsize=(10,6),dpi=70)
colors = ['#ff9999','#ffcc99']
ax.pie(x,labels=labels,colors=colors, autopct = '%1.1f%%', startangle=90) 
plt.title("Exang",fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.axis('equal')
plt.show()


# Graph: Target vs Exang

# In[47]:


pclass_xt = pd.crosstab(data['target'], data['exang'])
pclass_xt.astype('int64')


# In[48]:


pclass_xt = pd.crosstab(data["exang"], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against exang')
plt.legend()
plt.show()


# Graph: Number of slope vs exang

# In[49]:


pclass_xt = pd.crosstab(data['slope'], data['exang'])
pclass_xt.astype('int64')


# In[50]:


pclass_xt = pd.crosstab(data["exang"], data["slope"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of slope')
plt.title('Number of slope against exang')
plt.legend()
plt.show()


# Graph: Target vs Oldpeak

# In[51]:


x=data['oldpeak']
y=data['target']
plt.figure(figsize=(10,5))
plt.scatter(x,y)
plt.title('Target against Oldpeak')
plt.xlabel('oldpeak')
plt.ylabel('target')
plt.show()


# Graph: Pie chart of slope

# In[52]:


x = list(data['slope'].value_counts())
labels = list(data['slope'].value_counts().index)
plt.subplots(figsize=(10,6),dpi=70)
colors = ['#66b3ff','teal','cyan']
plt.pie(x,labels=labels,colors=colors, autopct = '%1.1f%%', startangle=90) 
plt.title("slope",fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.axis('equal')
plt.show()


# Graph: Target vs Slope

# In[53]:


pclass_xt = pd.crosstab(data['target'], data['slope'])
pclass_xt.astype('int64')


# In[54]:


pclass_xt = pd.crosstab(data["slope"], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against slope')
plt.legend()
plt.show()


# Graph: Pie chart of ca

# In[55]:


x = list(data['ca'].value_counts())
labels = list(data['ca'].value_counts().index)
plt.subplots(figsize=(10,6),dpi=70)
colors = ['salmon','lime','yellow','orange','orchid']
plt.pie(x,labels=labels,colors=colors, autopct = '%1.1f%%', startangle=90) 
plt.title("ca",fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.axis('equal')
plt.show()


# Graph: Target vs ca

# In[56]:


pclass_xt = pd.crosstab(data['target'], data['ca'])
pclass_xt.astype('int64')


# In[57]:


pclass_xt = pd.crosstab(data["ca"], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against ca')
plt.legend()
plt.show()


# Graph: Number of thal

# In[58]:


data['thal'].value_counts().plot(kind='bar')
plt.title('Number of thal')
plt.xlabel('thal')
plt.ylabel('total')
plt.show()


# Graph: Target vs thal

# In[59]:


pclass_xt = pd.crosstab(data['target'], data['thal'])
pclass_xt.astype('int64')


# In[60]:


pclass_xt = pd.crosstab(data['thal'], data["target"]) 
pclass_xt.plot(kind='bar', stacked=True)
plt.ylabel('number of target')
plt.title('Number of target against thal')
plt.legend()
plt.show()


# Graph: Pie chart of target

# In[61]:


x = list(data['target'].value_counts())
labels = list(data['target'].value_counts().index)
plt.subplots(figsize=(10,6),dpi=70)
colors = ['gold','silver']
plt.pie(x,labels=labels,colors=colors, autopct = '%1.1f%%', startangle=90) 
plt.title("target",fontsize=18)
plt.legend(loc='upper right',fontsize=15)
plt.axis('equal')
plt.show()

