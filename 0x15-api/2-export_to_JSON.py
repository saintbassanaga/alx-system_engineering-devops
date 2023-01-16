#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    records = []
    user = requests.get(endpoint + "users/{}".
                        format(userId)).json()
    todo = requests.get(endpoint + "todos?userId={}".
                        format(userId)).json()
    for task in todo:
        records.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })
    data = {
        "{}".format(userId): records
    }

    with open("{}.json".format(userId), 'w') as f:
        json.dump(data, f)
