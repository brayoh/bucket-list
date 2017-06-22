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
        item_id = (self.items[len(self.items)-1]['id'] + 1) if len(self.items) > 0 else id + 1
        item = {
            "id": item_id,
            "bucketlist_id":bucketlist_id,
            "name": name,
            "done": False,
            "created_at": datetime.utcnow().isoformat()
        }
        total_items = len(self.items)
        self.items.append(item)

        # check if items list has incremented to be sure that user was added
        return True, item if total_items < len(self.items) else False


    """ update an item
        parameters: item id, item to update, new item value
    """
    def update_item(self, update_type, update_value):
        if any(btype == update_type for btype in ["created_at", "id", "bucketlist_id"]):
            return False, "invalid field"
        else:
            for item in self.items:
                if update_type in dict.keys(item):
                    item[update_type] = update_value
                    return True, blist_item
                    break
            else:
                return "item not found"


    """ get items for a specific bucketlist
        parameters: user_id
    """
    def get_bucketlist_items(self, bucketlist_id):
        items = []
        for item in self.items:
            if bucketlist_id == item['bucketlist_id']:
                items.append(blist)
        return items


    """ get bucketlist items for a specific user using bucketlist_id
        parameters: user_id
    """
    def get_item_by_id(self, item_id):
        for item in self.items:
            if int(item_id) == item['id']:
                return blist
                break
        else:
            return False

    """ check if item exists
        parameters: item_id
    """
    def check_item_exists(self, item_id):
        return any((int(item['id']) == int(item_id)) for item in self.items)


    """ delete item
        parameters: item id
    """
    def delete_item(self, item_id):
        for item in self.items:
            if int(item_id) == int(item['id']):
                self.items.remove(item)
                return True
            break
        return "item not found"
