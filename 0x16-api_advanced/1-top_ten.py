#!/usr/bin/python3
"""
This module fetches and prints the titles of the top 10 hot posts from a
specified subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the top 10 hot posts from a specified
    subreddit. If the subreddit name is not a string or is None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    reddit_url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    request_headers = {'User-Agent': 'Iriele Moses/ALX-Api-Advanced'}
    request_params = {'limit': 10}

    try:
        response = requests.get(reddit_url, headers=request_headers,
                                params=request_params)
        response_data = response.json().get('data')

        for post in response_data.get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
