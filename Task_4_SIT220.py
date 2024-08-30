#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[7]:


import numpy as np
import pandas as pd
pd.set_option("display.notebook_repr_html", False)
df = pd.read_csv('data/weather.csv')
df['temp'] = (df['temp'] - 32) * (5/9)
df['dewp'] = (df['dewp'] - 32) * (5/9)
df['precip'] = df['precip'] * 25.4
df['visib'] = df['visib'] * 1609.34
df['wind_speed'] = df['wind_speed'] * 0.44704
df['wind_gust'] = df['wind_gust'] * 0.44704
df


# # Question 2

# In[8]:


df_lga = df[df['origin'] == 'LGA']
daily_mean_wind_speed = df_lga.groupby(['year', 'month', 'day'])['wind_speed'].mean().reset_index()
daily_mean_wind_speed.rename(columns={'wind_speed': 'daily_mean_wind_speed'}, inplace=True)
daily_mean_wind_speed


# # Question 3

# In[9]:


import matplotlib.pyplot as plt
import streamlit as st

# Assuming daily_mean_wind_speed is your DataFrame
daily_mean_wind_speed['date'] = pd.to_datetime(daily_mean_wind_speed[['year', 'month', 'day']])

# Create the plot
fig, ax = plt.subplots()
ax.plot(daily_mean_wind_speed['date'], daily_mean_wind_speed['daily_mean_wind_speed'])

ax.set_title('Daily Mean Wind Speeds at LGA Airport (2013)')
ax.set_xlabel('day')
ax.set_ylabel('daily average wind speed [m/s] at LGA')

ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m'))
ax.xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator(interval=2))

# Display the plot in the Streamlit app
st.pyplot(fig)


# # Question 4

# In[10]:


top_10_windiest_days = daily_mean_wind_speed.sort_values(by='daily_mean_wind_speed', ascending=False).head(10)
top_10_windiest_days = top_10_windiest_days.drop(columns=['year', 'month', 'day'])
top_10_windiest_days = top_10_windiest_days.set_index('date')
top_10_windiest_days


# In[ ]:




