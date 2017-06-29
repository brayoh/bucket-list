""" This class contains tests for AccountsManager class
"""
import unittest
from app.accounts_manager import AccountsManager


class AccountsManagerTest(unittest.TestCase):
    """  docstring for LoginTest """
    def setUp(self):
        self.account_manager = AccountsManager()

    def tearDown(self):
        self.account_manager = None

    # test other aspects
    def test_creates_new_user(self):
        user = self.account_manager.signup("brian", "password")
        self.assertTrue(user, "user should be able to sign up")

    def test_return_false_if_password_wrong(self):
        result = self.account_manager.login("brian", "pssord")
        self.assertFalse(result)

    def test_return_false_if_password_empty(self):
        result = self.account_manager.login("brian", "")
        self.assertFalse(result)

    def test_return_false_if_inputs_empty(self):
        result = self.account_manager.login("", "")
        self.assertFalse(result)

    def test_return_true_if_user_exists(self):
        user = self.account_manager.signup("brian", "password")
        check = self.account_manager.check_user_exists("brian")
        self.assertTrue(check)

    def test_return_false_if_user_doesnt_exist(self):
        user = self.account_manager.signup("brian", "password")
        check = self.account_manager.check_user_exists("bria")
        self.assertFalse(check)

    def test_increments_user_id(self):
        user = self.account_manager.signup("brian", "password")
        user2 = self.account_manager.signup("john", "pass")
        user_id = self.account_manager.get_user_id("john")
        self.assertEqual(user_id, 2)

    def test_returns_user_id(self):
        user = self.account_manager.signup("brian", "password")
        user_id = self.account_manager.get_user_id("brian")
        self.assertEqual(user_id, 1)

    def test_user_returns_false_for_unregistered(self):
        user = self.account_manager.signup("brian", "password")
        user_id = self.account_manager.get_user_id("doe")
        self.assertFalse(user_id)

    def test_duplicate_username(self):
        user1 = self.account_manager.login("brian", "new password")
        user2 = self.account_manager.login("brian", "new password")
        self.assertFalse(user2)

    def test_logins_in_user(self):
        self.account_manager.signup("brian", "password")
        login_user = self.account_manager.login("brian", "password")
        self.assertTrue(login_user, "user should be able to login")

    def test_returns_false_for_unregistered_user(self):
        result = self.account_manager.login("jane", "doe")
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()
