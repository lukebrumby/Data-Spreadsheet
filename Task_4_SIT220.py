#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

# Question 1
pd.set_option("display.notebook_repr_html", False)
df = pd.read_csv('data/weather.csv')
df['temp'] = (df['temp'] - 32) * (5/9)
df['dewp'] = (df['dewp'] - 32) * (5/9)
df['precip'] = df['precip'] * 25.4
df['visib'] = df['visib'] * 1609.34
df['wind_speed'] = df['wind_speed'] * 0.44704
df['wind_gust'] = df['wind_gust'] * 0.44704
st.write(df)

# Question 2
df_lga = df[df['origin'] == 'LGA']
daily_mean_wind_speed = df_lga.groupby(['year', 'month', 'day'])['wind_speed'].mean().reset_index()
daily_mean_wind_speed.rename(columns={'wind_speed': 'daily_mean_wind_speed'}, inplace=True)
st.write(daily_mean_wind_speed)

# Question 3 - Using Altair for mobile-friendly plotting
daily_mean_wind_speed['date'] = pd.to_datetime(daily_mean_wind_speed[['year', 'month', 'day']])

chart = alt.Chart(daily_mean_wind_speed).mark_line().encode(
    x=alt.X('date:T', title='Date', axis=alt.Axis(format='%Y-%m')),
    y=alt.Y('daily_mean_wind_speed:Q', title='Daily Average Wind Speed [m/s]')
).properties(
    title='Daily Mean Wind Speeds at LGA Airport (2013)',
    width='container',
    height=400
).interactive()  # Makes the plot zoomable and scrollable on mobile

st.altair_chart(chart)

# Question 4
top_10_windiest_days = daily_mean_wind_speed.sort_values(by='daily_mean_wind_speed', ascending=False).head(10)
top_10_windiest_days = top_10_windiest_days.drop(columns=['year', 'month', 'day'])
top_10_windiest_days = top_10_windiest_days.set_index('date')
st.write(top_10_windiest_days)
