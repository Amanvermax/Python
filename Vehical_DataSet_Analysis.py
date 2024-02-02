#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\TARANG PATEL\Downloads\vehicles.csv",encoding='unicode_escape')
df


# In[6]:


df.sort_values('city08')


# In[7]:


df.sort_values(
by ='city08',
ascending=False
)


# In[10]:


df.sort_values(
by=['city08',"highway08"]
)[['city08',"highway08"]]


# In[11]:


df.sort_index(axis=1)


# # FUEL TYPES

# In[18]:


avg_mpg_by_fuel_type = df.groupby('fuelType')['highway08'].mean()
print(avg_mpg_by_fuel_type)
 


# In[28]:


plt.figure(figsize=(8, 5))
df['fuelType'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Distribution of Fuel Types")
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.show()


# # CORRELATION FOR DISPLACMENT AND FUEL EFFICIENCY

# In[19]:


correlation_displ_mpg = df['displ'].corr(df['comb08'])
print(f"Correlation between engine displacement and fuel efficiency: {correlation_displ_mpg}")


# In[21]:


correlation_displ_mpg = df['displ'].corr(df['comb08'])
print(f"Correlation between engine displacement and fuel efficiency: {correlation_displ_mpg}")
 
plt.figure(figsize=(10, 6))
plt.scatter(df['displ'], df['comb08'], alpha=0.5)
plt.title('Scatter Plot of Engine Displacement vs. Fuel Efficiency')
plt.xlabel('Engine Displacement (liters)')
plt.ylabel('Combined Fuel Efficiency (mpg)')
plt.grid(True)
plt.show()


# # AVG MILEAGE BY YEAR

# In[24]:


avg_mpg_by_year = df.groupby('year')['comb08'].mean()
print(avg_mpg_by_year)


# In[26]:


import matplotlib.pyplot as plt
 
avg_mpg_by_year = df.groupby('year')['comb08'].mean()
 
plt.figure(figsize=(12, 6))
avg_mpg_by_year.plot(kind='bar', color='skyblue')
plt.title('Average Fuel Efficiency by Year')
plt.xlabel('Year')
plt.ylabel('Average Combined Fuel Efficiency (mpg)')
plt.grid(axis='y')
plt.show()


# # Chart Showing Barrels in Different City

# In[23]:


from matplotlib import pyplot as plt
plt.bar(df["barrels08"],df["city08"])
plt.xlabel("barrels08")
plt.ylabel("city08")
plt.show()


# # Number of electric vehicles

# In[30]:


num_evs = df[df['fuelType'] == 'Electricity'].shape[0]
print(f"Number of electric vehicles: {num_evs}")


# In[34]:


import matplotlib.pyplot as plt
 
ev_df = df[df['fuelType'] == 'Electricity']
 
ev_counts = ev_df['make'].value_counts()
 
plt.figure(figsize=(10, 6))

ev_counts.plot(kind='bar')

plt.title('Number of Electric Vehicles by Manufacturer')

plt.xlabel('Manufacturer')

plt.ylabel('Number of Electric Vehicles')

plt.xticks(rotation=45, ha='right')  

plt.tight_layout()

plt.show()


# In[45]:





# # Plotting the distribution of transmission types

# In[47]:


plt.figure(figsize=(8, 5))
df['trany'].value_counts().plot(kind='bar', color='orange')
plt.title("Distribution of Transmission Types")
plt.xlabel("Transmission Type")
plt.ylabel("Count")
plt.show()


# # Plotting a bar chart of vehicle class distribution

# In[48]:


plt.figure(figsize=(10, 6))
sns.countplot(x='VClass', data=df)
plt.xticks(rotation=90)
plt.xlabel('Vehicle Class')
plt.ylabel('Count')
plt.title('Distribution of Vehicles by Class')
plt.show()


# # Average fuel efficiency over the years

# In[52]:


avg_mpg_by_year = df.groupby('year')['comb08'].mean()
plt.plot(avg_mpg_by_year)
plt.xlabel('Year')
plt.ylabel('Average MPG')
plt.title('Average Fuel Efficiency Over the Years')
plt.show()


# # Relationship between highway and city MPG

# In[53]:


plt.scatter(df['highway08'], df['city08'])
plt.xlabel('Highway MPG')
plt.ylabel('City MPG')
plt.title('Relationship between Highway and City MPG')
plt.show()


# # Box plot to compare fuel efficiency between different drive types
# 

# In[54]:


plt.figure(figsize=(12, 6))
sns.boxplot(x='drive', y='comb08', data=data)
plt.title("Fuel Efficiency Comparison by Drive Type")
plt.xlabel("Drive Type")
plt.ylabel("Combined MPG")
plt.show()


# In[ ]:




