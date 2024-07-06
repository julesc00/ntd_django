from http import HTTPStatus
import requests


class APIClient:
    def __init__(self, url, query):
        self.url = url
        self.query = query

    def get(self):
        res = requests.post(self.url, json={'query': self.query})
        if res.status_code == HTTPStatus.OK:
            return res.json()
        return res.raise_for_status()
