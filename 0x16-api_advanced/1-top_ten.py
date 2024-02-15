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

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for text in range(10):
            print(data[text].get('data').get('title'))
    else:
        print("None")
