import unittest
from app.bucketlist import BucketList
from app.accounts_manager import AccountsManager


class TestBucketListCrud(unittest.TestCase):
    """ docstring for TestBucketListCrud."""
    def setUp(self):
        self.bucketlist = BucketList()
        self.account_manager = AccountsManager()

    def tearDown(self):
        self.bucketlist = None

    def test_creates_bucket_list(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        result = self.bucketlist.create_bucket_list(user_id,
                                                    "dare devil",
                                                    "try out experiences")
        self.assertEqual(result, True, "should create a new bucketlist")

    def test_gets_user_bucket_list(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        result = self.bucketlist.create_bucket_list(user_id,
                                                    "dare devil",
                                                    "try out experiences")
        blist = self.bucketlist.get_user_bucketlists(user_id)
        self.assertGreater(len(blist), 0)

    def test_gets_user_bucket_list_by_id(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        result = self.bucketlist.create_bucket_list(user_id,
                                                    "dare devil",
                                                    "try out experiences")
        blist_id = self.bucketlist.get_bucketlist_id(user_id,"dare devil")
        blist = self.bucketlist.get_bucketlist_by_id(user_id, blist_id)
        self.assertGreater(len(blist), 0)

    def test_returns_false_if_name_is_empty(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        result = self.bucketlist.create_bucket_list(user_id,
                                                    "",
                                                    "try out experiences")
        self.assertEqual(result, False)

    def test_returns_false_if_description_is_empty(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        result = self.bucketlist.create_bucket_list(user_id, "dare devil", "")
        self.assertEqual(result, False)

    def test_returns_false_if_input_is_empty(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        result = self.bucketlist.create_bucket_list(user_id, "", "")
        self.assertEqual(result, False)

    def test_returns_false_if_all_inputs_are_empty(self):
        result = self.bucketlist.create_bucket_list("", "", "")
        self.assertEqual(result, False)

    def test_throws_exception_if_id_is_not_an_integer(self):
        with self.assertRaises(TypeError):
            self.bucketlist.create_bucket_list([],
                                               "dare devil",
                                               "try thrilling experiences")

    def test_updates_bucket_list_name(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        blist = self.bucketlist.create_bucket_list(user_id,
                                                   "dare devil",
                                                   "try thrilling experiences")
        bucketlist_id = self.bucketlist.get_bucketlist_id(user_id,
                                                          "dare devil")
        result = self.bucketlist.update_bucket_list(bucketlist_id,
                                                    "graduate",
                                                    "get a degreee")
        self.assertEqual(result, True)

    def test_updates_bucket_list_description(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        blist = self.bucketlist.create_bucket_list(user_id,
                                                   "dare devil",
                                                   "try thrilling experiences")
        bucketlist_id = self.bucketlist.get_bucketlist_id(user_id,
                                                          "dare devil")
        result = self.bucketlist.update_bucket_list(bucketlist_id,
                                                    "dare devil",
                                                    "try something new")
        self.assertEqual(result, True)

    def test_deletes_bucket_list_item(self):
        self.account_manager.signup("jane", "doe")
        user_id = self.account_manager.get_user_id("jane")
        blist = self.bucketlist.create_bucket_list(user_id,
                                                   "dare devil",
                                                   "try thrilling experiences")
        bucketlist_id = self.bucketlist.get_bucketlist_id(user_id,
                                                          "dare devil")
        result = self.bucketlist.delete_bucket_list(bucketlist_id)
        self.assertEqual(result, True)
