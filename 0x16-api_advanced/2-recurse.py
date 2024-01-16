#!/usr/bin/python3

import requests as req


def recurse(subreddit_name, post_titles=[], next_page=""):
    """
    This function recursively fetches the titles of hot posts for a
    given subreddit. If the subreddit does not exist, it returns None.
    """
    reddit_url = "http://www.reddit.com/r/{}/hot.json".format(subreddit_name)
    user_agent_header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firfox/73.0"
    }
    pagination_param = {
        "after": next_page,
        "limit": 100,
    }
    response_obj = req.get(reddit_url, headers=user_agent_header,
                           params=pagination_param, allow_redirects=False)
    if response_obj.status_code == 404:
        return None
    else:
        post_data = responde_obj.json().get("data").get("children")
        post_titles += [post.get("data").get("title") for post in post_data]
        next_page = response_obj.json().get("data").get("after")
        if next_page is not None:
            recurse(subreddit_name, post_titles, next_page)
        return post_titles
