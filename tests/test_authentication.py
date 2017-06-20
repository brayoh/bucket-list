import unittest
from app.authentication import Authentication


class AuthenticationTest(unittest.TestCase):
    """  docstring for LoginTest """
    def setUp(self):
        self.auth = Authentication()

    def test_creates_new_user(self):
        user = self.auth.signup("brian", "password")
        self.assertTrue(user, "user should be able to sign up")

    def test_logins_in_user(self):
        self.auth.signup("brian", "password")
        login_user = self.auth.login("brian", "password")
        self.assertTrue(login_user, "user should be able to login")

    def test_returns_false_if_password_wrong(self):
        result = self.auth.login("brian", "pssord")
        self.assertEqual(result, False)

    def test_returns_false_for_unregistered_user(self):
        result = self.auth.login("jane", "doe")
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()
