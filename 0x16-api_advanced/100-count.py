#!/usr/bin/python3
"""
This module contains a recursive function that interacts with the Reddit API.
It parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces. For example, 'Javascript'
should count as 'javascript', but 'java' should not). If no posts match or
the subreddit is invalid, it prints nothing.
"""

import requests


def count_words(subreddit_name, keyword_list, next_page_token='',
                keyword_dict={}):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints
    a sorted count of given keywords. If the subreddit name is not a string
    or is None, it returns None.
    """
    if not keyword_dict:
        for keyword in keyword_list:
            if keyword.lower() not in keyword_dict:
                keyword_dict[keyword.lower()] = 0

    if next_page_token is None:
        sorted_keywords = sorted(keyword_dict.items(), key=lambda x:
                                 (-x[1], x[0]))
        for keyword in sorted_keywords:
            if keyword[1]:
                print('{}: {}'.format(keyword[0], keyword[1]))
        return None

    reddit_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit_name)
    request_headers = {'user-agent': 'redquery'}
    request_params = {'limit': 100, 'after': next_page_token}
    response = requests.get(reddit_url, headers=request_headers,
                            params=request_params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot_posts = response.json()['data']['children']
        next_page_token = response.json()['data']['after']
        for post in hot_posts:
            title = post['data']['title']
            lower_case_title_words = [word.lower() for word in
                                      title.split(' ')]

            for keyword in keyword_dict.keys():
                keyword_dict[keyword] += lower_case_title_words.count(keyword)

    except Exception:
        return None

    count_words(subreddit_name, keyword_list, next_page_token, keyword_dict)
