from infra.base_api import BaseApi

class UsersApi(BaseApi):

    def add_user(self, user_data):
        return self.request("POST", "/users/add", json=user_data)

    def update_user(self, user_id, new_data):
        return self.request("PUT", f"/users/{user_id}", json=new_data)

    def delete_user(self, user_id):
        return self.request("DELETE", f"/users/{user_id}")
    def search_user(self, query):
        return self.request("GET", f"/users/search?q={query}")