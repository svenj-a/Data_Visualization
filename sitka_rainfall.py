# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:26:06 2023

@author: Studi
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Get rainfall data for Sitka.
filename_s = 'data/sitka_weather_2018_simple.csv'
with open(filename_s) as fs:
    reader = csv.reader(fs)
    header_row = next(reader)
       
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    # Get dates and rainfall data from this file.
    dates_s, prcp_s = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_s.append(current_date)
            prcp_s.append(rain)

# Plot the rainfall in sitka against the rainfall in death valley.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_s, prcp_s, c='green', alpha=0.8)

# Format plot.
title = "Daily amount of rainfall in Sitka, Alaska"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
# plt.ylim([0, 3.0])

plt.show()
