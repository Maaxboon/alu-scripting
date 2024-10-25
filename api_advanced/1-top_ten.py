import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json().get("data", {})
            posts = data.get("children", [])
            
            # Print the title of each post
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except Exception:
        print(None)
