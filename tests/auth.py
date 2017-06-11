import unittest
from app.authentication import Authentication

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.auth = Authentication()

    def test_creates_new_user(self):
        result = self.auth.create_user("brian","password")
        self.assertEqual(result, True)

    def test_logins_in_user(self):
        result = self.auth.login("brian", "password")
        self.assertEqual(result, True)

    def test_returns_false_if_password_wrong(self):
        result = self.auth.login("brian", "pssord")
        self.assertFalse(result)

    def test_returns_error_if_user_doesnt_exit(self):
        result = self.auth.login("john", "doe")
        self.assertEqual("user doesnt exist", result)

    def test_creates_bucket_list(self):
        result = self.auth.create_bucket_list("brian", "visit the niagra falls")
        self.assertEqual(result, True)

    def test_updates_bucket_list_item(self):
        result = self.auth.update_bucket_list_item("brian", "visit the niagra falls", "swim with the dolphins")
        self.assertEqual(result, True)

    def test_deletes_bucket_list_item(self):
        result = self.auth.delete_bucket_list_item("brian", "visit the niagra falls")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
