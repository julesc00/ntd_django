from http import HTTPStatus
import requests


class APIClient:
    """
    A simple API client to fetch data from the GraphQL API.
    """
    def __init__(self, url, query):
        self.url = url
        self.query = query

    def get(self):
        """
        Get data from the API.
        """
        res = requests.post(self.url, json={'query': self.query})
        if res.status_code == HTTPStatus.OK:
            return res.json()
        return res.raise_for_status()
