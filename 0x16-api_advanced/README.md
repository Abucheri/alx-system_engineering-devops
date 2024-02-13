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

1. Top Ten 
	- Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.
	- Requirements:
		- Prototype: `def top_ten(subreddit)`
		- If not a valid subreddit, print None.
		- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
	```
	wintermancer@lapbox ~/reddit_api/project $ cat 1-main.py
	#!/usr/bin/python3
	"""
	1-main
	"""
	import sys

	if __name__ == '__main__':
	    top_ten = __import__('1-top_ten').top_ten
	    if len(sys.argv) < 2:
	        print("Please pass an argument for the subreddit to search.")
	    else:
	        top_ten(sys.argv[1])
	wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py programming
	Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
	How a 64k intro is made
	HTTPS on Stack Overflow: The End of a Long Road
	Spend effort on your Git commits
	It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
	From the D Blog: Introspection, Introspection Everywhere
	Do MVC like it’s 1979
	GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
	Google Bug Bounty - The 5k Error Page
	PyCon 2017 Talk Videos
	wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py this_is_a_fake_subreddit
	None
	wintermancer@lapbox ~/reddit_api/project $ 
	```
