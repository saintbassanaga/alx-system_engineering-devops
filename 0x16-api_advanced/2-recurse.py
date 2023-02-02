#!/usr/bin/python3
"""Get subreddit all posts"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries subreddit api"""
    import requests

    data = requests.get(
        "https://www.reddit.com/r/{}/hot.json"
        .format(subreddit),
        params={"count": count, "after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    if data.status_code >= 400:
        return None

    hot_posts = hot_list + [
        post.get('data').get('title')
        for post in data.json().get("data").get("children")
    ]

    if not data.json().get('data').get('after'):
        return hot_posts

    return recurse(
        subreddit,
        hot_posts,
        data.json().get('data').get('count'),
        data.json().get('data').get('after')
                 )
