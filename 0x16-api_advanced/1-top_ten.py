#!/bin/usr/python3
"""
Write a function prints the titles of the first 10 hot post Reddit API
"""
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "Frocuts"}
    endpoint = "http://reddit.com/r/{}/hot.json?limit=10"
    subs = requests.get(endpoint.format(subreddit), headers=headers)
    if subs.status_code != 200:
        print(None)
        return 0
    subs = subs.json()
    if subs["kind"] == "Listing":
        for data in (subs["data"]["children"]):
            print(data["data"]["title"])
    else:
        print(None)
