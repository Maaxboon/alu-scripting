#!/usr/bin/python3
"""Module for retrieving top 10 hot posts from a subreddit."""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the top 10 hot posts
    for a given subreddit."""
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if subreddit exists by verifying a 200 status code
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            # Output titles or `None` if there are no posts
            if data:
                for post in data:
                    print(post.get("data", {}).get("title"))
            else:
                print("None")
        else:
            print("None")

    except requests.exceptions.RequestException:
        print("None")
