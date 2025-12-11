import unittest
from logic.products_api import ProductsApi

class TestGetSingleProduct(unittest.TestCase):

    def test_get_single(self):
        api = ProductsApi()

        res = api.get_single_product(1)

        self.assertTrue(res.success)
        self.assertEqual(res.get("id"), 1)
