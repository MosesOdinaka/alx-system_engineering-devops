#!/usr/bin/python3
"""
This module contains a function that interacts with the Reddit API to fetch
the number of subscribers for a specific subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Fetches and returns the number of subscribers for a specified subreddit.
    If the subreddit name is not a string or is None, it returns 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    reddit_url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    request_headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/Iriele Odinaka)'
    }

    response = requests.get(reddit_url, headers=request_headers).json()

    try:
        subscriber_count = response.get('data').get('subscribers')
        return subscriber_count
    except Exception:
        return 0
