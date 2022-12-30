# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:50:14 2022

@author: svenj
"""

import matplotlib.pyplot as plt

# Define x and y values.
x_val = range(1, 5001)
y_val = [x**3 for x in x_val]

# Create plots as subplots and set a chart style.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_val, y_val, c=y_val, cmap='inferno', s= 10)

# Set chart title and label axes.
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axes.
ax.axis([0, 5100, 0, 130000000000])

plt.show()
