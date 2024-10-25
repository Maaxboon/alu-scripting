#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

def top_ten(subreddit):
    """Fetch and print the top ten hot post titles for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            json_data = response.json()
            posts = json_data.get('data', {}).get('children', [])
            
            # Print up to the first 10 post titles
            for i in range(min(10, len(posts))):
                print(posts[i].get('data', {}).get('title'))
        else:
            print("Subreddit not found or access is restricted.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")