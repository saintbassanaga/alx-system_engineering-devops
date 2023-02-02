#!/usr/bin/python3
"""Get subreddit users"""


def number_of_subscribers(subreddit):
    """Queries subreddit api"""
    import requests

    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code >= 300:
        return 0

    return data.json().get("data").get("subscribers")
