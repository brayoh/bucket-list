import unittest
from app.bucketlist import BucketList


class TestBucketListCrud(unittest.TestCase):
    """ docstring for TestBucketListCrud."""
    def setUp(self):
        self.bucket = BucketList()

    def test_creates_bucket_list(self):
        result = self.bucket.create_bucket_list("visit the niagra falls")
        self.assertEqual(result, True, "should create a new bucketlist")

    def test_updates_bucket_list_item(self):
        blist = self.bucket.create_bucket_list("visit the niagra falls")
        result = self.bucket.update_bucket_list_item("visit the niagra falls",
                                                     "swim with the dolphins")
        self.assertEqual(result, True)

    def test_deletes_bucket_list_item(self):
        blist = self.bucket.create_bucket_list("visit the niagra falls")
        result = self.bucket.delete_bucket_list_item("visit the niagra falls")
        self.assertEqual(result, True)
