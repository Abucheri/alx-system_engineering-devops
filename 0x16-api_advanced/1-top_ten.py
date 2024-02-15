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
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Python/requests'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Raise an HTTPError for bad responses
        response.raise_for_status()

        data = response.json().get('data', {}).get('children', [])
        if not data:
            print("None")
            return

        for post in data[:10]:
            title = post.get('data', {}).get('title')
            print(title)
    except requests.exceptions.HTTPError:
        print("None")
    except requests.exceptions.RequestException:
        print("None")
    except (ValueError, AttributeError):
        print("None")
