import unittest
from logic.products_api import ProductsApi

class TestSearchProducts(unittest.TestCase):

    def test_search(self):
        api = ProductsApi()
        res = api.search_products("phone")

        self.assertTrue(res.success)
        self.assertGreater(len(res.get("products", [])), 0)
