#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code != 200:
        return 0
    dictionary = result.json()
    if 'data' not in dictionary:
        return 0
    if 'subscribers' not in dictionary.get('data'):
        return 0
    return result.json()['data']['subscribers']
