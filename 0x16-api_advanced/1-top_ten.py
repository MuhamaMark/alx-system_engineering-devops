#!/usr/bin/python3
"""
function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """ Queries the Reddit API and Returns 1st 10"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}

    result = requests.get(url, headers=headers,
                          params=params, allow_redirects=False)
    if result.status_code != 200:
        print(None)
        return
    dictn = result.json()
    hot_posts = dictn['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
