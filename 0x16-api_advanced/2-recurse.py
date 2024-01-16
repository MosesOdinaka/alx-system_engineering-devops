#!/usr/bin/python3
"""
This module contains a recursive function that interacts with the Reddit API.
It returns a list of titles for all hot articles from a specified subreddit.
"""

import requests

def recurse(subreddit_name, hot_titles=[], after_token=""):
    """
    Queries the Reddit API and fetches the titles of all hot articles from a
    specified subreddit. If the subreddit name is not a string or is None,
    it returns None.
    """
    if subreddit_name is None or not isinstance(subreddit_name, str):
        return None

    reddit_url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit_name)
    request_headers = {'User-Agent': 'ALX-advanced_APIi/by Iriele Moses'}
    request_params = {
            'after': after_token,
            'limit': 100
            }

    response = requests.get(reddit_url, headers=request_headers, params=request_params,
                            allow_redirects=True)

    if response.status_code == 404:
        return None

    response_data = response.json().get('data')
    after_token = response_data.get('after')

    for post in response_data.get('children'):
        hot_titles.append(post.get('data').get('title'))

    if after_token is not None:
        return recurse(subreddit_name, hot_titles, after_token)
    
    return hot_titles
