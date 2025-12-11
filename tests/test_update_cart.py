import unittest
from logic.carts_api import CartsApi
from infra.config_loader import Config

class TestUpdateCart(unittest.TestCase):

    def test_update_cart(self):
        api = CartsApi()
        payload = Config.load()["update_cart"]

        res = api.update_cart(1, payload)

        self.assertTrue(res.success)
        self.assertIsInstance(res.get("products"), list)
