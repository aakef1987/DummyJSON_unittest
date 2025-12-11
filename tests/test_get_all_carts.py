import unittest
from logic.carts_api import CartsApi

class TestGetAllCarts(unittest.TestCase):

    def test_get_all_carts(self):
        api = CartsApi()
        res = api.get_all_carts()

        self.assertTrue(res.success)
        self.assertGreater(len(res.get("carts", [])), 0)
