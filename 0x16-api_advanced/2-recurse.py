#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0'}

    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        data = response.json()

        if 'error' in data:
            return None

        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except (requests.RequestException, KeyError):
        return None
