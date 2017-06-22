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

    def test_creates_new_user(self):
        user = self.account_manager.signup("brian", "password")
        self.assertTrue(user, "user should be able to sign up")

    def test_returns_false_if_password_wrong(self):
        result = self.account_manager.login("brian", "pssord")
        self.assertFalse(result)

    def test_returns_false_if_password_empty(self):
        result = self.account_manager.login("brian", "")
        self.assertFalse(result)

    def test_returns_false_if_username_empty(self):
        result = self.account_manager.login("", "pass")
        self.assertFalse(result)

    def test_returns_false_if_both_empty(self):
        result = self.account_manager.login("", "")
        self.assertFalse(result)

    def test_logins_in_user(self):
        self.account_manager.signup("brian", "password")
        login_user = self.account_manager.login("brian", "password")
        self.assertTrue(login_user, "user should be able to login")

    def test_returns_false_for_unregistered_user(self):
        result = self.account_manager.login("jane", "doe")
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()
