#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


fig , axes = plt.subplots(2,3,figsize = (16,8))

#Linear Chart
years = np.array([2010,2011,2012,2013,2014,2015])
apples = np.array([0.895,0.91,0.9190,0.926,0.929,0.931])
oranges = np.array([0.962, 0.941, 0.930, 0.923, 0.918, 0.908])
axes[0,0].plot(years, apples, 's-b')
axes[0,0].plot(years, oranges, 'o--r')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Yield (tons per hectare)')
axes[0,0].legend(['Apples', 'Oranges']);
axes[0,0].set_title('Crop Yields in Kanto')

#Scatter Plot
#The Iris flower dataset provides samples measurements of sepals and petals for 3 species of flowers. 
#The Iris dataset is included with the Seaborn library, and can be loaded as a Pandas data frame.
flowers_df = sns.load_dataset("iris")
sns.scatterplot(flowers_df.sepal_length, 
                flowers_df.sepal_width, 
                hue=flowers_df.species, 
                s=100, 
                ax=axes[0,1]);

#Histogram
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
axes[0,2].set_title('Distribution of Sepal Width')
axes[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True);
axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica']);


#Barplot
#Let's look at another sample dataset included with Seaborn, called "tips". 
#The dataset contains information about the sex, time of day, total bill and tip amount for customers visiting a restaurant over a week
tips_df = sns.load_dataset("tips");
axes[1,0].set_title('Restaurant bills')
sns.barplot('day', 'total_bill', hue='sex', data=tips_df, ax=axes[1,0]);

#Heatmap
flights_df = sns.load_dataset("flights").pivot("month","year","passengers")
flights_df
axes[1,1].set_title('Flight traffic')
sns.heatmap(flights_df, cmap='Blues',annot = True ,ax=axes[1,1]);

#Image
from PIL import Image
img = Image.open('chart.jpg')
axes[1,2].set_title('Data Science Meme')
axes[1,2].imshow(img)
axes[1,2].grid(False)

plt.tight_layout(pad=2)


# In[2]:


import jovian
jovian.commit(project = 'matplotlib_subplots')


# In[ ]:




