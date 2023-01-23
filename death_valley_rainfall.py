# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:26:06 2023

@author: Studi
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Get rainfall data for Death Valley.
filename_d = 'data/death_valley_2018_simple.csv'
with open(filename_d) as fd:
    reader = csv.reader(fd)
    header_row = next(reader)
       
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    # Get dates and rainfall data from this file.
    dates_d, prcp_d = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            prcp_d.append(0)
        else:
            dates_d.append(current_date)
            prcp_d.append(rain)

# Plot the rainfall in sitka against the rainfall in death valley.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_d, prcp_d, c='orange', alpha=0.8)

# Format plot.
title = "Daily amount of rainfall in Death Valley, CA"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
# plt.ylim([0, 3.0])

plt.show()
