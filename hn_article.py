# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:55:46 2023

@author: Studi
"""

import requests
import json

# Make an API call, and store the response.
#url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
#url = 'https://hacker-news.firebaseio.com/v0/item/35107579.json'
url = 'https://hacker-news.firebaseio.com/v0/item/35107238.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
#readable_file = 'data/readable_hn_data.json'
#readable_file = 'data/readable_hn_data2.json'
readable_file = 'data/readable_hn_data3.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
