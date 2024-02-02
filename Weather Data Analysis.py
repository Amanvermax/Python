#!/usr/bin/env python
# coding: utf-8

# In[45]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\TARANG PATEL\Downloads\1. Weather Data.csv",encoding='unicode_escape')
df


# In[9]:


df.shape


# In[10]:


df['Weather'].unique()


# In[16]:


df['Wind Speed_km/h'].count()


# # Highest temprature date

# In[35]:


df['Date/Time'] = pd.to_datetime(df['Date/Time'])

max_temp_row = df.loc[df['Temp_C'].idxmax()]

print("Date with the highest temperature:")
print(max_temp_row['Date/Time'])
print("Highest Temperature:", max_temp_row['Temp_C'])


# In[27]:


df['Date/Time'] = pd.to_datetime(df['Date/Time'])

plt.figure(figsize=(12, 6))
plt.plot(df['Date/Time'], df['Temp_C'], marker='o', linestyle='-', color='b')
plt.title('Temperature Over Time')
plt.xlabel('Date/Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# # Hiighest visiblity  Day

# In[29]:


df['Date/Time'] = pd.to_datetime(df['Date/Time'])

max_visiblity_row = df.loc[df['Visibility_km'].idxmax()]

print("Date with the highest visiblity KM:")
print(max_visiblity_row['Date/Time'])
print("Highest visiliblity:", max_temp_row['Visibility_km'])


# # Wind speed less then 15 table

# In[37]:


filtered_df = df[df['Wind Speed_km/h'] < 15]

print(filtered_df)


# In[41]:


ltered_df = df[df['Wind Speed_km/h'] < 15]

plt.figure(figsize=(10, 6))
plt.bar(filtered_df['Date/Time'], filtered_df['Wind Speed_km/h'], color='green')
plt.title('Wind Speed Less Than 15 km/h')
plt.xlabel('Date/Time')
plt.ylabel('Wind Speed (km/h)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# In[42]:


from matplotlib import pyplot as plt

plt.scatter(df["Date/Time"],df["Temp_C"])
plt.title("visibilty with temprature")
plt.ylabel("Date/Time")
plt.xlabel("Temprature")
plt.show()


# In[48]:


df.corr()[['Temp_C']]


# In[46]:


sns.heatmap(df.corr(),annot = True)


# # Top 10 highest wind speeds

# In[49]:


import matplotlib.pyplot as plt
 
 
top10_df = df.nlargest(10, 'Wind Speed_km/h')
 
 
plt.bar(top10_df['Date/Time'], top10_df['Wind Speed_km/h'])
plt.xlabel('Date/Time')
plt.ylabel('Wind Speed (km/h)')
plt.title('Top 10 Highest Wind Speeds')
plt.xticks(rotation=45)
plt.show()


# # Lowest Pressure Date

# In[50]:


min_pressure_index = df['Press_kPa'].idxmin()
date_min_pressure = df.loc[min_pressure_index, 'Date/Time']
print(f"\nDate with the Lowest Pressure: {date_min_pressure}")


# # Wind Speed Distrubtion

# In[53]:


wind_speed_distribution = df['Wind Speed_km/h'].value_counts().sort_index()
print("\nWind Speed Distribution:")
print(wind_speed_distribution)


# In[54]:


wind_speed_distribution = df['Wind Speed_km/h'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
wind_speed_distribution.plot(kind='bar', color='blue')
plt.title('Wind Speed Distribution')
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()


# # Find out the maximum speed of wind where Weather = Foggy

# In[52]:


import pandas as pd
fog_data = df[df['Weather'] == 'Fog']
max_wind_speed_in_fog = fog_data['Wind Speed_km/h'].max()
print("Maximum wind speed during foggy weather:", max_wind_speed_in_fog)


# In[ ]:




