import requests

from infra.response_wrapper import ResponseWrapper


class BaseApi:
    BASE_URL = "https://dummyjson.com"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        return ResponseWrapper(response)
