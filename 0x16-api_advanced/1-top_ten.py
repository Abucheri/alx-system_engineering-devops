#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()

        if 'error' in data:
            print(None)
        else:
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
    except (requests.RequestException, KeyError):
        print(None)
