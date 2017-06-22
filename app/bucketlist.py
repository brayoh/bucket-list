from datetime import datetime
id = 0


class BucketList(object):
    """This class will handle creation, updating, retrieval and deleting of BucketLists """
    def __init__(self):
        self.bucketlist = []

    """ create a new bucketlist
        parameters: user id, bucketlist name, bucketlist description
    """
    def create_bucket_list(self, user_id, name, description):
        bucketlist_id = (self.bucketlist[len(self.bucketlist)-1]['id'] + 1) if len(self.bucketlist) > 0 else id + 1
        total_items = len(self.bucketlist)
        try:
            if all(len(value) > 0 for value in [name, description]):
                if self.check_bucketlist_name_exists(name):
                    return False

                user_id = int(user_id)
                bucketlist = {
                    "id": bucketlist_id,
                    "user_id": user_id,
                    "name": name,
                    "description": description,
                    "created_at": datetime.utcnow().isoformat()
                }
                self.bucketlist.append(bucketlist)
                print(self.bucketlist)
            else:
                return False
            return True if total_items < len(self.bucketlist) else False
        except TypeError:
            raise TypeError("user id should be integer")

        # check if bucketlist list has incremented to be sure that user was added


    """ update a bucketlist
        parameters: bucketlist id, item to update, new item value
    """
    def update_bucket_list(self, bucketlist_id, name, description):

        for blist in self.bucketlist:
            if bucketlist_id == blist['id']:
                blist['name'] = name
                blist['description'] = description
                return True
                break
        else:
            return "bucketlist not found"


    """ get bucketlist items for a specific user
        parameters: user_id
    """
    def get_user_bucketlists(self, user_id):
        bucketlists = []

        for blist in self.bucketlist:
            if user_id == blist['user_id']:
                bucketlists.append(blist)
        return bucketlists


    """ get bucketlist items for a specific user using bucketlist_id
        parameters: user_id
    """
    def get_bucketlist_by_id(self, user_id, bucketlist_id):
        for blist in self.bucketlist:
            if user_id == blist['user_id'] and bucketlist_id == blist['id']:
                return blist
                break
        else:
            return False


    """ get bucketlist items for a specific user using bucketlist_id
        parameters: user_id
    """
    def get_bucketlist_id(self, user_id, bucketlist_name):
        for blist in self.bucketlist:
            if user_id == blist['user_id'] and bucketlist_name == blist['name']:
                return blist['id']
                break
        else:
            return False


    """ check if bucketlist exists
        parameters: bucketlist_id
    """
    def check_bucketlist_exists(self, bucketlist_id):
        return any((int(blist['id']) == int(bucketlist_id)) for blist in self.bucketlist)


    """ check if bucketlist name exists
        parameters: bucketlist_id
    """
    def check_bucketlist_name_exists(self, name):
        return any(blist['name'] == name for blist in self.bucketlist)


    """ delete bucketlist
        parameters: bucketlist id
    """
    def delete_bucket_list(self, bucketlist_id):
        for blist_item in self.bucketlist:
            if int(bucketlist_id) == int(blist_item['id']):
                self.bucketlist.remove(blist_item)
                return True
            break
        return "bucketlist not found"
