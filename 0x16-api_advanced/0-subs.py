#!/usr/bin/python3
"""
0-subs
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    # Set a custom User-Agent
    headers = {'User-Agent': 'Python/requests'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        return data['data']['subscribers']
    except (requests.RequestException, KeyError):
        return 0
