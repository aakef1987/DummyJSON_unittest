import unittest
from logic.products_api import ProductsApi
from infra.config_loader import Config

class TestUpdateProduct(unittest.TestCase):

    def test_update_product(self):
        api = ProductsApi()
        data = Config.load()["update_product"]

        res = api.update_product(1, data)

        self.assertTrue(res.success)
        self.assertEqual(res.get("title"), data["title"])
