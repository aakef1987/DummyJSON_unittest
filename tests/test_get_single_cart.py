import unittest
from logic.carts_api import CartsApi

class TestGetSingleCart(unittest.TestCase):

    def test_get_single_cart(self):
        api = CartsApi()
        res = api.get_single_cart(1)

        self.assertTrue(res.success)
        self.assertEqual(res.get("id"), 1)
