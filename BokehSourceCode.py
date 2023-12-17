#!/usr/bin/env python
# coding: utf-8

# # Installation

# In[32]:


get_ipython().system('pip install pandas-bokeh')


# # Import Libraries
# 

# In[33]:


import pandas as pd #working on data frames
import numpy as np
import pandas_bokeh #implement bokeh on pandas data frame
from bokeh.io import show, output_notebook #show various data plotting 
from bokeh.plotting import figure #various graphs
import glob #merge files and get it in the required format 
import time
from time import process_time #calculate the time 
pandas_bokeh.output_notebook() #output in notebook
pd.set_option('plotting.backend', 'pandas_bokeh')


# # Import data

# In[34]:


data =pd.read_csv("C:/Users/Anisha/Downloads/Computer Science/CPC152/heart_disease.csv.csv")


# In[35]:


data


# # Data Analysis 

# Step 1: Understanding data 

# In[36]:


data.head() #show first five rows


# In[37]:


data.tail() #shows last five rows 


# In[38]:


data.shape #checking the number of rows and columns 


# In[39]:


data.describe() #summary of decriptive stats on numerical values data only


# In[40]:


data.columns #shows the columns involved in the dataset 


# In[41]:


data.nunique()


# In[42]:


#dtype: int64, tells us that python is storing each value within this columns as 64 bit integer 


# In[43]:


data ['age'].unique()


# In[44]:


data['sex'].unique()


# In[45]:


data['cp'].unique()


# In[46]:


data['trestbps'].unique()


# In[47]:


data['chol'].unique()


# In[48]:


data['fbs'].unique()


# In[49]:


data['restecg'].unique()


# In[50]:


data['thalach'].unique()


# In[51]:


data['exang'].unique()


# In[52]:


data['oldpeak'].unique()


# In[53]:


data['ca'].unique()


# In[54]:


data['thal'].unique()


# In[55]:


data['target'].unique()


# Step 2: Cleaning data 

# In[56]:


data.isnull().sum()


# Step 3: Analysing data

# Graph: Age Distribution

# In[57]:


data['age'].unique()


# In[58]:


data_age = data['age'].astype('int64')


# In[59]:


#Start the stopwatch/counter
t1_start = process_time()
data_age.plot_bokeh(kind='hist', title = "Distribution Of Age")

#Stop the stopwatch / counter
t1_stop = process_time()
print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)


# Graph: Age vs Chol

# In[60]:


data['age'].unique()


# In[61]:


data['chol'].unique()


# In[62]:


#from bokeh.plotting import figure, output_file, show
        
# file to save the model
#output_file("gfg.html")
        
# instantiating the figure object
graph = figure(title = "Scatter Graph: Age vs Chol ")

#name of x-axis
graph.xaxis.axis_label = 'chol'

#name of y-axis
graph.yaxis.axis_label='age'
      
# the points to be plotted
x = data['chol']
y = data['age']
     
# plotting the graph
graph.scatter(x, y)
      
# displaying the model
show(graph)


# Graph: Age vs Exang

# In[63]:


data['exang'].unique()


# In[64]:


data['age'].unique()


# In[65]:


data_age_ex = pd.crosstab(data['exang'], data['age'])
data_age_ex


# In[66]:


data_age_ex.plot_bokeh.bar(title = "Age vs Exang")


# Graph: Age vs Target

# In[67]:


data['age'].unique()


# In[68]:


data['target'].unique()


# In[69]:


data_age_tar = pd.crosstab(data['target'], data['age'])
data_age_tar.astype('int64')


# In[70]:


data_age_tar.plot_bokeh.bar(title = "Age vs Target")


# Graph: age vs oldpeak

# In[71]:


data['oldpeak'].unique()


# In[72]:


# importing the modules
#from bokeh.plotting import figure, output_file, show
import random
  
# file to save the model
#output_file("gfg.html")
   
# instantiating the figure object
graph = figure(title = "Line Graph: age vs oldpeak", toolbar_location ='below')
  
# name of the x-axis
graph.xaxis.axis_label = "age"
  
# name of the y-axis
graph.yaxis.axis_label = "oldpeak"
  
# plotting line 1
# generating the points to be plotted
x = []
y = []
for i in range(100):
    x.append(i)
for i in range(100):
    y.append(1 + random.random())
  
# parameters of line 1
line_color = "red"
line_dash = "solid"
legend_label = "Line 1"
  
# plotting the line
graph.line(x, y,
           line_color = line_color,
           line_dash = line_dash,
           legend_label = legend_label)
  

   
# displaying the model
show(graph)


# Graph (Sex vs Target)

# In[73]:


data_sex_tar = pd.crosstab(data['target'], data['sex'])
data_sex_tar.astype('int64')


# In[74]:


data_sex_tar.plot_bokeh.bar(title = "Sex vs Target")


# Graph (CP vs Target)

# In[75]:


data['cp'].unique()


# In[76]:


data_cp_tar = pd.crosstab(data['target'], data['cp'])
data_cp_tar.astype('int64')


# In[77]:


data_cp_tar.plot_bokeh.bar(title = "CP vs Target")


# In[78]:


data_cp_tar = pd.crosstab(data['target'], data['cp'])
data_cp_tar.astype('int64')


# In[79]:


data_cp_tar.plot_bokeh.pie(title = "CP vs Target")


# Graph: Target vs trestbps

# In[80]:


data['trestbps'].unique()


# In[81]:


data_trest_tar = pd.crosstab(data['trestbps'], data['target'])
data_trest_tar.astype('int64')


# In[82]:


data_trest_tar.plot_bokeh.bar(title = "Trestbps vs Target")


# In[83]:


#To analyse graph values clearly, please zoom in. 


# Graph: Chol vs Target

# In[84]:


data_chol_tar = pd.crosstab(data['chol'], data['target'])
data_chol_tar.astype('int64')


# In[85]:


data_chol_tar.plot_bokeh.bar(title = "Chol vs Target")


# In[86]:


#To analyse graph values clearly, please zoom in. 


# Graph: fbs vs Target

# In[87]:


data['fbs'].unique()


# In[88]:


data_fbs_tar = pd.crosstab(data['fbs'], data['target'])
data_fbs_tar.astype('int64')


# In[89]:


data_fbs_tar.plot_bokeh.bar(title = "fbs vs Target")


# In[90]:


data_fbs_tar.plot_bokeh.pie(title = "fbs vs Target")


# Graph: restecg vs Target

# In[91]:


data['restecg'].unique()


# In[92]:


data_ecg_tar = pd.crosstab(data['restecg'], data['target'])
data_ecg_tar.astype('int64')


# In[93]:


data_ecg_tar.plot_bokeh.bar(title = "restecg vs Target")


# In[94]:


data_ecg_tar.plot_bokeh.pie(title = "restecg vs Target")


# Graph: thalach vs Target

# In[95]:


data['thalach'].unique()


# In[96]:


data_tha_tar = pd.crosstab(data['thalach'], data['target'])
data_tha_tar.astype('int64')


# In[97]:


data_tha_tar.plot_bokeh.bar(title = "thalach vs Target")


# In[98]:


#To see graph clearly, please zoom in. 


# Graph: exang vs Target

# In[99]:


data['exang'].unique()


# In[100]:


data_ex_tar = pd.crosstab(data['exang'], data['target'])
data_ex_tar.astype('int64')


# In[101]:


data_ex_tar.plot_bokeh.bar(title = "exang vs Target")


# In[102]:


data_ex_tar.plot_bokeh.pie(title = "exang vs Target")


# Graph: oldpeak vs Target

# In[103]:


data['oldpeak'].unique()


# In[104]:


data_old_tar = pd.crosstab(data['oldpeak'], data['target'])
data_old_tar.astype('int64')


# In[105]:


data_old_tar.plot_bokeh.bar(title = "oldpeak vs Target")


# In[106]:


#To analyse graph clearly, please zoom in. 


# Graph: slope vs Target

# In[107]:


data['slope'].unique()


# In[108]:


data_slope_tar = pd.crosstab(data['slope'], data['target'])
data_slope_tar.astype('int64')


# In[109]:


data_slope_tar.plot_bokeh.bar(title = "slope vs Target")


# In[110]:


data_slope_tar.plot_bokeh.pie(title = "slope vs Target")


# Graph: ca vs Target

# In[111]:


data['ca'].unique()


# In[112]:


data_ca_tar = pd.crosstab(data['ca'], data['target'])
data_ca_tar.astype('int64')


# In[113]:


data_ca_tar.plot_bokeh.bar(title = "ca vs Target")


# In[114]:


data_ca_tar.plot_bokeh.pie(title = "ca vs Target")


# Graph: thal vs Target

# In[115]:


data['thal'].unique()


# In[116]:


data_thal_tar = pd.crosstab(data['thal'], data['target'])
data_thal_tar.astype('int64')


# In[117]:


data_thal_tar.plot_bokeh.bar(title = "thal vs Target")


# In[118]:


data_thal_tar.plot_bokeh.pie(title = "thal vs Target")


# In[ ]:




