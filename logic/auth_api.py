from infra.base_api import BaseApi

class AuthApi(BaseApi):

    def login(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        return self.request("POST", "/auth/login", json=payload)
