#!/usr/bin/env python
# coding: utf-8

# # Line Chart
# 
# 

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib inline is use to ensure that plots are shown and embedded within the Jupyter notebook itself. 
#Without this command, sometimes plots may show up in pop-up windows.


# Yield of apples (tons per hectare) over 6 years in an imaginary country called Kanto.

# In[17]:


years = np.array([2010,2011,2012,2013,2014,2015])
yield_apples = np.array([0.895,0.91,0.9190,0.926,0.929,0.931])


# We can visualize how the yield of apples changes over time using a line chart

# In[20]:


plt.plot(years,yield_apples)
plt.xlabel('Year')
plt.ylabel('Yield(tons per hectare)')


# Let's compare the yield of apples versus the yield of oranges in Kanto

# In[75]:


years = range(2000,2012)
apples = np.array([0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939])
oranges = np.array([0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ])
plt.plot(years,apples,marker = 'o',c='b', ls='-', lw=2, ms=8, mew=2, mec='navy',mfc = 'pink')
plt.plot(years,oranges,marker = 'x',c='r', ls='--', lw=3, ms=10, alpha=.5)
plt.xlabel('Year')
plt.ylabel('Yield(tons per hectare)')
plt.title("Crop Yields in Kanto")
plt.legend(['Apples','Oranges']);


# The fmt argument provides a shorthand for specifying the line style, marker and line color. It can be provided as the third argument to plt.plot.
# 
# fmt = '[marker][line][color]'

# In[76]:


plt.plot(years, apples, 's-b')# s for square
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges']);


# If no line style is specified in fmt, only markers are drawn

# In[77]:


plt.figure(figsize = (8,4))
plt.plot(years,oranges,'or')
plt.title("Yield of Oranges(tons per hectare)")


# An easy way to make your charts look beautiful is to use some default styles provided in the Seaborn library. These can be applied globally using the sns.set_style function

# In[78]:


sns.set_style('whitegrid')


# In[79]:


plt.plot(years,apples,'s-b')
plt.plot(years,oranges,'o--r')
plt.xlabel('Years')
plt.ylabel('Years(tons per hectare)')
plt.title("Crop yields in Kanto")
plt.legend(['Apples','Oranges'])


# You can also edit default styles directly by modifying the matplotlib.rcParams dictionary

# In[80]:


plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (9,5)
plt.rcParams['figure.facecolor'] = '#00000000'
plt.plot(years, oranges, 'or')
plt.title("Yield of Oranges (tons per hectare)");


# In[81]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[82]:


import jovian


# In[83]:


jovian.commit(project='python-matplotlib-data-visualization')


# # Scatter plot

# The Iris flower dataset provides samples measurements of sepals and petals for 3 species of flowers. The Iris dataset is included with the Seaborn library, and can be loaded as a Pandas data frame

# In[84]:


# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")


# In[85]:


flowers_df


# In[86]:


flowers_df.species.unique()


# In[87]:


plt.plot(flowers_df.sepal_length,flowers_df.sepal_width);


# In[89]:


plt.scatter(flowers_df.sepal_length,flowers_df.sepal_width);


# In[91]:


sns.scatterplot(flowers_df.sepal_length,flowers_df.sepal_width)


# Notice how the points in the above plot seem to form distinct clusters with some outliers. We can color the dots using the flower species as a hue. We can also make the points larger using the s argument.
# 
# 

# In[94]:


plt.figure(figsize=(12, 6))
plt.title('Sepal Dimensions')
sns.scatterplot(flowers_df.sepal_length,flowers_df.sepal_width,hue = flowers_df.species,s = 100);


# Seaborn has in-built support for Pandas data frames. Instead of passing each column as a series, you can also pass column names and use the data argument to pass the data frame

# In[95]:


plt.title('Sepal Dimensions')
sns.scatterplot('sepal_length', 
                'sepal_width', 
                hue='species',
                s=100,
                data=flowers_df);


# # Histogram

# In[96]:


plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width)


# We can control the number of bins, or the size of each bin using the bins argument.

# In[97]:


plt.hist(flowers_df.sepal_width,bins = 5)


# In[100]:


import numpy as np
plt.hist('sepal_width',bins = np.arange(2,5,0.25),data = flowers_df)


# Similar to line charts, we can draw multiple histograms in a single chart. We can reduce the opacity of each histogram, so the the bars of one histogram don't hide the bars for others.
# 
# Let's draw separate histograms for each species of flowers.

# In[101]:


setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']


# In[105]:


plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));


# We can also stack multiple histograms on top of one another.

# In[106]:


plt.title('Distribution of Sepal Width')

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']);


# # Bar chart

# In[108]:


years = range(2000, 2006)
apples = np.array([0.35, 0.6, 0.9, 0.8, 0.65, 0.8])
oranges = np.array([0.4, 0.8, 0.9, 0.7, 0.6, 0.8])


# In[109]:


plt.bar(years, oranges);


# Like histograms, bars can also be stacked on top of one another. We use the bottom argument to plt.bar to achieve this.

# In[110]:


plt.bar(years, apples)
plt.bar(years, oranges, bottom=apples);


# # Bar chart with Averages

# Let's look at another sample dataset included with Seaborn, called "tips". The dataset contains information about the sex, time of day, total bill and tip amount for customers visiting a restaurant over a week.
# 

# In[112]:


tips = sns.load_dataset("tips");


# In[113]:


tips_df


# In[114]:


sns.barplot('day','total_bill',data = tips_df);


# The lines cutting each bar represent the amount of variation in the values. For instance, it seems like the variation in the total bill was quite high on Fridays, and lower on Saturday

# In[116]:


sns.barplot('day','total_bill',hue = 'sex',data = tips_df);


# # Heatmap

# A heatmap is used to visualize 2-dimensional data like a matrix or a table using colors. The best way to understand it is by looking at an example. We'll use another sample dataset from Seaborn, called "flights", to visualize monthly passenger footfall at an airport over 12 years.

# In[117]:


flights_df = sns.load_dataset("flights").pivot("month","year","passengers")
flights_df


# flights_df is a matrix with one row for each month and one column of each year. The values in the matrix show the number of passengers (in thousands) that visited the airport in a specific month of a specific year. We can use the sns.heatmap function to visualize the footfall at the airport.

# In[118]:


plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df);


# The brighter colors indicate a higher footfall at the airport. By looking at the graph, we can infer two things:
# 
# The footfall at the airport in any given year tends to be the highest around July & August.
# The footfall at the airport in any given month tends to grow year by year.

# We can also display the actual values in each block by specifying annot=True, and use the cmap argument to change the color palette.

# In[119]:


plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues');


# # Images

# In[120]:


from urllib.request import urlretrieve
urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg');


# Before an image can be displayed, it has to be read into memory using the PIL module

# PIL = python imaging library

# Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. 

# In[122]:


from PIL import Image


# In[123]:


img = Image.open('chart.jpg')


# An image loaded using PIL is simply a 3-dimensional numpy array containing pixel intensities for the red, green & blue (RGB) channels of the image. We can convert the image into an array using np.array.
# 
# 

# In[124]:


img_array = np.array(img)
img_array.shape
plt.imshow(img);


# In[125]:


plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img);


# To display a part of the image, we can simply select a slice from the numpy array.
# 
# 

# In[126]:


plt.grid(False)
plt.axis('off')
plt.imshow(img_array[125:325,105:305]);


# # Pair plots with seaborn

# Seaborn also provides a helper function sns.pairplot to automatically plot different types of charts for pairs of features within a dataframe.

# In[128]:


sns.pairplot(flowers_df, hue='species');


# In[ ]:




