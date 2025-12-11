import unittest
from logic.products_api import ProductsApi

class TestGetAllProducts(unittest.TestCase):

    def test_get_all(self):
        api = ProductsApi()
        res = api.get_all_products()

        self.assertTrue(res.success)
        self.assertGreater(len(res.get("products", [])), 0)
