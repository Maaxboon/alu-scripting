#!/usr/bin/python3
"""Print the titles of the first 10 hot posts in a subreddit"""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of the top 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for valid response (status code 200) and parse titles
    if response.status_code == 200:
        json_data = response.json().get("data", {}).get("children", [])
        if json_data:
            for post in json_data[:10]:
                print(post["data"].get("title"))
        else:
            print("None")
    else:
        print("None")
