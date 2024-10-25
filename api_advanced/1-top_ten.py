#!/usr/bin/python3
"""Module for task 1"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the top 10 hot posts
    of the subreddit."""
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is valid
    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post.get("data", {}).get("title"))
    else:
        # Print None if subreddit does not exist
        print("None")
