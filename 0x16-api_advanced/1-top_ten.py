#!/usr/bin/python3
"""Get subreddit posts"""


def top_ten(subreddit):
    """Queries subreddit api"""
    import requests

    data = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code >= 300:
        print("None")
        return

    for post in data.json().get("data").get("children")[:10]:
        print(post.get('data').get('title'))


if __name__ == '__main__':
    top_ten('asdasdasdsad')
