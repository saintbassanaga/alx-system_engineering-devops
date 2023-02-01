#!/usr/bin/python3

"""
Write a function that queries the Reddit API and returns the number of subscribers

"""

import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;\
                         rv:68.0) Gecko/20100101 FirefoxFirefox/68.0'}
    with requests.session() as client:
        info = client.get(url, headers=headers, allow_redirects=False).json()
        return info.get('data', {}).get('subscribers', 0)
