import json
import os
import requests


def setUp():
    """Add data to server, so short url links can be used.
    """
    file = open(f'{filePath}/fixtures/urls.json')
    data = json.load(file)

    for i in data:
        payload = json.dumps({
            "url": i['url']
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request(
            "POST",
            f"{server}/api/link",
            headers=headers,
            data=payload)
        res = response.json()
        i['id'] = res['id']


if __name__ == "__main__":
    server = "http://localhost:5000"
    filePath = os.path.dirname(os.path.realpath(__file__))
    setUp()
