#!/usr/bin/python3
"""
Contains the top_ten function to query Reddit API and print titles of 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }

    try:
        # Prevents redirects to search results for invalid subreddits
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        
        # Check if subreddit exists by checking the status code
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            if len(data) == 0:
                print(None)
                return

            for post in data:
                print(post.get("data", {}).get("title"))

        else:
            print(None)

    except requests.RequestException:
        print(None)
