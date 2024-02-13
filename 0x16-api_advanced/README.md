#  0x16. API advanced 

![WIxXad8](https://github.com/Abucheri/alx-system_engineering-devops/assets/24778489/712c6821-158f-44d4-bb53-666446d60e80)


## Background Context
<p>
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.
</p>

 0. How many subs? 
	- Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
	- Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.
	- Requirements:
		- Prototype: `def number_of_subscribers(subreddit)`
		- If not a valid subreddit, return 0.
		- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
	```
	wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
	#!/usr/bin/python3
	"""
	0-main
	"""
	import sys

	if __name__ == '__main__':
	    number_of_subscribers = __import__('0-subs').number_of_subscribers
	    if len(sys.argv) < 2:
	        print("Please pass an argument for the subreddit to search.")
	    else:
	        print("{:d}".format(number_of_subscribers(sys.argv[1])))
	wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
	756024
	wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
	0
	```
