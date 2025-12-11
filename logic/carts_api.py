from infra.base_api import BaseApi

class CartsApi(BaseApi):

    def get_all_carts(self):
        return self.request("GET", "/carts")

    def get_single_cart(self, cart_id):
        return self.request("GET", f"/carts/{cart_id}")

    def add_cart(self, cart_data):
        return self.request("POST", "/carts/add", json=cart_data)

    def update_cart(self, cart_id, new_data):
        return self.request("PUT", f"/carts/{cart_id}", json=new_data)

    def delete_cart(self, cart_id):
        return self.request("DELETE", f"/carts/{cart_id}")
