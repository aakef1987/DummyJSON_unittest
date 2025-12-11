import unittest
from logic.users_api import UsersApi

class TestSearchUser(unittest.TestCase):

    def test_search_user(self):
        api = UsersApi()
        res = api.search_user("John")

        self.assertTrue(res.success)
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.get("users", [])), 0)
