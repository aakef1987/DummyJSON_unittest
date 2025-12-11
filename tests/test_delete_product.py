import unittest
from logic.products_api import ProductsApi

class TestDeleteProduct(unittest.TestCase):

    def test_delete_product(self):
        api = ProductsApi()

        res = api.delete_product(1)

        self.assertTrue(res.success)
        self.assertEqual(res.get("isDeleted"), True)
