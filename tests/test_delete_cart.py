import unittest
from logic.carts_api import CartsApi

class TestDeleteCart(unittest.TestCase):

    def test_delete_cart(self):
        api = CartsApi()

        res = api.delete_cart(1)

        self.assertTrue(res.success)
        self.assertEqual(res.get("isDeleted"), True)
