#!/usr/bin/env python
# coding: utf-8

# In[34]:





# In[35]:


from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv('dataset-83422.csv')

#box plot
b=df.Price
plt.title("boxplot")
plt.xlabel("price")
sns.boxplot(b)
plt.legend()
plt.show()


#histogram to check the transmission frequency
a=df['MPG.city']
plt.title("histogram")
plt.xlabel("miles per galoon")
plt.hist(a,bins=5,edgecolor='black')
plt.legend()
plt.show()

#scatter plot to find relation of   horsepower and weight

x=df['Horsepower']
y=df['Weight']
plt.scatter(x,y)
plt.xlabel('horsepower')
plt.ylabel('weight')
plt.title('scatterplot')
plt.legend()
plt.show()

#line chart to engine size agains horsepower

m=df['Width']
plt.title("line chart")
plt.xlabel('width')
plt.ylabel('horsepower')
sns.lineplot(m,x)
plt.show()








# In[ ]:




