#!/usr/bin/python3
"""
100-count
"""

import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Abucheri)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        data = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = data.get("data")
    after = data.get("after")
    count += data.get("dist")
    for text in data.get("children"):
        title = text.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                ocurr = len([txt for txt in title if txt == word.lower()])
                if instances.get(word) is None:
                    instances[word] = ocurr
                else:
                    instances[word] += ocurr

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
