""" BucketList Class"""
from datetime import datetime
ID = 0


class BucketList(object):
    """ This class will handle creation, updating, retrieval
    and deleting of BucketLists"""
    def __init__(self):
        self.bucketlist = []

    def create_bucket_list(self, user_id, name, description):
        """ create a new bucketlist
        parameters: user id, bucketlist name, bucketlist description """
        if len(self.bucketlist) > 0:
            last_item = self.bucketlist[len(self.bucketlist)-1]
            bucketlist_id = (last_item['id'] + 1)
        else:
            bucketlist_id = ID + 1
        total_items = len(self.bucketlist)
        try:
            if all(len(value) > 0 for value in [name, description]):
                if self.check_bucketlist_name_exists(name):
                    return False
                bucketlist = {
                    "id": bucketlist_id,
                    "user_id": int(user_id),
                    "name": name,
                    "description": description,
                    "created_at": datetime.utcnow().isoformat()
                }
                self.bucketlist.append(bucketlist)
            else:
                return False
            return True if total_items < len(self.bucketlist) else False
        except TypeError:
            raise TypeError("user id should be integer")

    def update_bucket_list(self, bucketlist_id, name, description):
        """ update a bucketlist
        parameters: bucketlist id, item to update, new item value"""

        for blist in self.bucketlist:
            if bucketlist_id == blist['id']:
                blist['name'] = name
                blist['description'] = description
                return True
                break
        else:
            return "bucketlist not found"

    def get_user_bucketlists(self, user_id):
        """ get bucketlist items for a specific user
        parameters: user_id """
        bucketlists = []

        for blist in self.bucketlist:
            if user_id == blist['user_id']:
                bucketlists.append(blist)
        return bucketlists

    def get_bucketlist_by_id(self, user_id, id):
        """ get bucketlist items for a specific user using bucketlist_id
        parameters: user_id
        """
        for blist in self.bucketlist:
            if user_id == blist['user_id'] and id == blist['id']:
                return blist
                break
        else:
            return False

    def get_bucketlist_id(self, user_id, name):
        """ get bucketlist items for a specific user using bucketlist id
        parameters: user_id """
        for blist in self.bucketlist:
            if user_id == blist['user_id'] and name == blist['name']:
                return blist['id']
                break
        else:
            return False

    def check_bucketlist_exists(self, id):
        """ check if bucketlist exists, parameters: bucketlist_id """
        return any((int(blist['id']) == int(id)) for blist in self.bucketlist)

    def check_bucketlist_name_exists(self, name):
        """ check if bucketlist name exists parameters: bucketlist_id """
        return any(blist['name'] == name for blist in self.bucketlist)

    def delete_bucket_list(self, bucketlist_id):
        """ delete bucketlist parameters: bucketlist id """
        for blist_item in self.bucketlist:
            if int(bucketlist_id) == int(blist_item['id']):
                self.bucketlist.remove(blist_item)
                return True
            break
        return "bucketlist not found"
