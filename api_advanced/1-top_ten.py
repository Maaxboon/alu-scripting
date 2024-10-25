#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    
    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if response is successful and contains data
        if response.status_code != 200:
            print(None)
            return
        
        hot_posts = response.json().get("data", {}).get("children", None)
        
        if not hot_posts:
            print(None)
        else:
            for post in hot_posts:
                print(post.get("data", {}).get("title"))
    except Exception:
        print(None)

# Make sure to remove trailing whitespace from blank lines
