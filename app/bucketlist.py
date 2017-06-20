class BucketList(object):
    """docstring for BucketList."""
    def __init__(self):
        self.bucketlist = []

    def create_bucket_list(self, item):
        self.bucketlist.append({'item': item, 'done': False})
        return True

    def update_bucket_list_item(self, item, updated_item):
        for blist_item in self.bucketlist:
            if item in dict.values(blist_item):
                blist_item['item'] = updated_item
                return True
            else:
                return "item not found"

    def delete_bucket_list_item(self, item):
        for blist_item in self.bucketlist:
            if item in dict.values(blist_item):
                self.bucketlist.remove(blist_item)
                return True
            break
        return "item not found"
