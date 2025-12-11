import unittest
from logic.auth_api import AuthApi

class TestLoginIncorrect(unittest.TestCase):

    def test_login_incorrect(self):
        api = AuthApi()

        res = api.login("wrongUser", "wrongPass")

        self.assertEqual(res.status_code, 400)
        self.assertFalse(res.success)
        self.assertEqual(res.get("message"), "Invalid credentials")
