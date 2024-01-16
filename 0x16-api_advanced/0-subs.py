#!/usr/bin/python3

import requests as req


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers for a given subreddit.
    If the subreddit does not exist, it returns 0.
    """
    reddit_url = "https://www.reddit.com/r/{}/about.json"
    .format(subreddit)
    headers_dict = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"
    }
    response_obj = req.get(reddit_url, headers=headers_dict,
                           allow_redirects=False)
    if response_obj.status_code == 404:
        return 0
    subreddit_data = response_obj.json().get("data")
    return subreddit_data.get("subscribers")
