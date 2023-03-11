# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:16:36 2023

@author: Studi
"""

from operator import itemgetter
from plotly import offline

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'id': str(response_dict['id']),
            'by': response_dict['by'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict["descendants"],
            }
    except KeyError:
        #print(f"KeyError for ID: {submission_id}")
        submission_dict = {
            'title': response_dict['title'],
            'id': str(response_dict['id']),
            'by': response_dict['by'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': 0,
            }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

subm_links, subm_commis, labels = [], [], []
for submission_dict in submission_dicts:
    subm_url = submission_dict['hn_link']
    subm_id = submission_dict['id']
    subm_link = f"<a href='{subm_url}'>{subm_id}</a>"
    subm_links.append(subm_link)
    subm_commis.append(submission_dict['comments'])
    labels.append(f"{submission_dict['title']}<br />{submission_dict['by']}")
    
    #print(f"\nTitle: {submission_dict['title']}")
    #print(f"Discussion link: {submission_dict['hn_link']}")
    #print(f"Comments: {submission_dict['comments']}")

# Make visualization.
data = [{
    'type': 'bar',
    'x': subm_links,
    'y': subm_commis,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(0, 102, 102)',
        'line': {'width': 1.5, 'color': 'rgb(0, 51, 51)'},
        },
    'opacity': 0.6,
    }]

my_layout = {
    'title': "Most Actively Discussed Articles on Hacker News",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_articles.html')
