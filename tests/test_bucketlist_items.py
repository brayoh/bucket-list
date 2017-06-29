import unittest
from controllers.bucketlist import BucketList
from controllers.bucketlist_items import BucketListItems
from controllers.accounts_manager import AccountsManager

class TestBucketListItems(unittest.TestCase):
    """ docstring for TestBucketListItems."""
    def setUp(self):
        self.bucketlist = BucketList()
        self.bucketlist_items = BucketListItems()
        self.account_manager = AccountsManager()
        self.user = self.account_manager.signup("brian", "password")
        user_id = self.account_manager.get_user_id("brian")
        self.bucketlist.create_bucket_list(user_id,
                                            "dare devil",
                                            "try out experiences")
        self.bucketlist_id = self.bucketlist.get_bucketlist_id(user_id, "dare devil")

    def tearDown(self):
        self.bucketlist = None

    def test_creates_new_item(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        self.assertTrue(item)
    def test_duplicate_items(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        item2 = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        self.assertFalse(item2)

    def test_updates_item(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        item_id = self.bucketlist_items.get_item_id("go bungee jumping")
        update = self.bucketlist_items.update_item(item_id, "go climbing", "not done")
        self.assertTrue(update)

    def test_doesnt_update_nonexisting_item(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        update = self.bucketlist_items.update_item(5, "go climbing", "not done")
        self.assertFalse(update)

    def test_gets_item_id(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        item_id = self.bucketlist_items.get_item_id("go bungee jumping")
        self.assertEqual(item_id, 1)

    def test_increments_item_id(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        item2 = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee")
        item_id = self.bucketlist_items.get_item_id("go bungee")
        self.assertEqual(item_id, 2)

    def test_returns_true_if_item_exists(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        item_id = self.bucketlist_items.get_item_id("go bungee jumping")
        exists = self.bucketlist_items.check_item_exists("go bungee jumping")
        self.assertTrue(exists)

    def test_deletes_item(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        item_id = self.bucketlist_items.get_item_id("go bungee jumping")
        deleted = self.bucketlist_items.delete_item(item_id)
        self.assertTrue(deleted)

    def test_doesnt_delete_nonexisting_item(self):
        item = self.bucketlist_items.create_item(self.bucketlist_id, "go bungee jumping")
        deleted = self.bucketlist_items.delete_item(10)
        self.assertFalse(deleted)
