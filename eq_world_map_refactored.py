# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:42:18 2023

@author: Studi
"""

import json

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    #readable_file = 'data/readable_eq_data.json'

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

map_title = all_eq_data['metadata']['title']
my_layout = Layout(title=map_title)
fig = {'data': data, 'layout': my_layout}
# error charmap codec \u25c4 is related to python version or anaconda env!
offline.plot(fig, filename='global_earthquakes_30.html')
