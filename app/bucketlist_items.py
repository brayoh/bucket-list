from datetime import datetime
id = 0


class BucketListItems(object):
    """docstring for BucketListItems."""
    def __init__(self):
        self.items = []

    """ create a new item
        parameters: user id, item's name, item's description
    """
    def create_item(self, bucketlist_id, name):

        if len(self.items) > 0:
            item_id = (self.items[len(self.items)-1]['id'] + 1)
        else:
            item_id = id + 1
        if self.check_item_exists(name):
            return False
        else:
            item = {
                "id": item_id,
                "bucketlist_id": bucketlist_id,
                "name": name,
                "done": "not done",
                "created_at": datetime.utcnow().isoformat()
            }
            total_items = len(self.items)
            self.items.append(item)
            return True, item if total_items < len(self.items) else False

    def update_item(self, item_id, name):
        """ update an item
        parameters: item id, new name
        """
        for item in self.items:
            if int(item_id) == item['id']:
                item['name'] = name
                return True
                break
        else:
            return "item not found"

    def get_items(self, bucketlist_id):
        """ get items for a specific bucketlist
        parameters: user_id
        """
        items = []
        for item in self.items:
            if bucketlist_id == item['bucketlist_id']:
                items.append(blist)
        return items

    def get_item_by_bucketlist_id(self, bucketlist_id):
        """ get bucketlist items for a specific user using bucketlist_id
        parameters: bucketlist_id
        """
        items = []
        for item in self.items:
            if int(bucketlist_id) == item['bucketlist_id']:
                items.append(item)
        return items

    def check_item_exists(self, item_name):
        """ check if item exists
        parameters: item_name
        """
        return any(item['name'] == item_name for item in self.items)

    def delete_item(self, item_id):
        """ delete item
        parameters: item id
        """
        for item in self.items:
            if int(item_id) == int(item['id']):
                self.items.remove(item)
                return True
                break
        return "item not found"
