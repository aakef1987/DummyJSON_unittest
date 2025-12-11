import unittest
from logic.users_api import UsersApi

class TestUpdateUser(unittest.TestCase):

    def test_update_user(self):
        api = UsersApi()

        # DummyJSON user 1 exists
        new_data = {
            "firstName": "EmilyUpdated",
            "age": 29
        }

        res = api.update_user(1, new_data)

        self.assertTrue(res.success)
        self.assertEqual(res.get("firstName"), "EmilyUpdated")
        self.assertEqual(res.get("age"), 29)
