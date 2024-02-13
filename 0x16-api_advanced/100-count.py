#!/usr/bin/python3
"""
100-count
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if counts is None:
        counts = {}

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0'}

    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        if 'error' in data:
            return

        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word = word.lower()
                if word not in counts:
                    counts[word] = 0
                counts[word] += title.count(word)

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            print_results(counts)
    except (requests.RequestException, KeyError, ValueError):
        return


def print_results(counts):
    """
    Prints the results in descending order by count and
    alphabetically for words with the same count.
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))
