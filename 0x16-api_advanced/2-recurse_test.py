#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after="", pages=0):
    """
    Recursively queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Abucheri)"
    }
    params = {
        "after": after,
        "pages": pages,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    pages += data.get("dist")
    for text in data.get("children"):
        hot_list.append(text.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, pages)
    return hot_list
