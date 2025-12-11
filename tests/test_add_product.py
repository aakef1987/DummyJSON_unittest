import unittest
from logic.products_api import ProductsApi
from infra.config_loader import Config

class TestAddProduct(unittest.TestCase):

    def test_add_product(self):
        api = ProductsApi()
        data = Config.load()["new_product"]

        res = api.add_product(data)

        self.assertTrue(res.success)
        self.assertEqual(res.get("title"), data["title"])
