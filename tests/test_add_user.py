import unittest
from logic.users_api import UsersApi

class TestAddUser(unittest.TestCase):

    def test_add_user(self):
        api = UsersApi()

        payload = {
            "firstName": "Muhammad",
            "lastName": "Ovi",
            "age": 30
        }

        res = api.add_user(payload)

        self.assertTrue(res.success)
        self.assertEqual(res.get("firstName"), "Muhammad")
