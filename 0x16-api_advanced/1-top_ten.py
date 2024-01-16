#!/usr/bin/python3

import requests as req


def top_ten(subreddit):
    """
    This function prints the titles of the top 10 posts for a given
    subreddit. If the sudreddit does not exist, it prints "None".
    """
    reddit_url = "http://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent_header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"
    }
    limit_param = {
        "limit": 10
    }
    response_obj = req.get(reddit_url, headers=user_agent_header,
                           params=limit_param, allow_redirects=False)
    if response_obj.status_code == 404:
        print("None")
        return
    subreddit_posts = response_obj.json().get("data")
    for post in subreddit_posts.get("children"):
        print(post.get("data").get("title"))
