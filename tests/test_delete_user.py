import unittest
from logic.users_api import UsersApi

class TestDeleteUser(unittest.TestCase):

    def test_delete_user(self):
        api = UsersApi()

        res = api.delete_user(1)

        self.assertTrue(res.success)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get("isDeleted"), True)
