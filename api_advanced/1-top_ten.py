#!/usr/bin/python3
"""Print the titles of the first 10Hot Posts"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'your-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        # Extract and print titles of the first 10 hot posts
    else:
        print(None)