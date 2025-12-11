from infra.base_api import BaseApi

class ProductsApi(BaseApi):

    def get_all_products(self):
        return self.request("GET", "/products")

    def get_single_product(self, product_id):
        return self.request("GET", f"/products/{product_id}")

    def search_products(self, query):
        return self.request("GET", f"/products/search?q={query}")

    def add_product(self, product_data):
        return self.request("POST", "/products/add", json=product_data)

    def update_product(self, product_id, new_data):
        return self.request("PUT", f"/products/{product_id}", json=new_data)

    def delete_product(self, product_id):
        return self.request("DELETE", f"/products/{product_id}")
