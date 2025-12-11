import unittest
from logic.carts_api import CartsApi
from infra.config_loader import Config

class TestAddCart(unittest.TestCase):

    def test_add_cart(self):
        api = CartsApi()
        payload = Config.load()["new_cart"]

        res = api.add_cart(payload)

        self.assertTrue(res.success)
        self.assertEqual(res.get("userId"), payload["userId"])
