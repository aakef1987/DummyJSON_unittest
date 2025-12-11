import unittest
from logic.auth_api import AuthApi

class TestLoginCorrect(unittest.TestCase):

    def test_login_correct(self):
        api = AuthApi()

        res = api.login("emilys", "emilyspass")

        self.assertTrue(res.success)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get("username"), "emilys")
