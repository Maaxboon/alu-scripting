#!/usr/bin/python3
"""Print the titles of the first 10 hot posts in a subreddit."""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of the top 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        
        # Check if there are posts; otherwise print None
        if data:
            for post in data[:10]:
                print(post["data"].get("title"))
        else:
            print("None")
    else:
        print("None")
