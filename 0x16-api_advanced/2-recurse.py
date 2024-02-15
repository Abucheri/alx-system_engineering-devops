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
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0'}

    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data").get("after")

        if data:
            after = data
            recurse(subreddit, hot_list, after)
        posts = response.json().get("data").get("children")
        for post in posts:
            title = post.get("data").get("title")
            hot_list.append(title)
        return hot_list
    else:
        return None
