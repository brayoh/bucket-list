import json

id = 0
users = []
bucketlist = []
logged_in = False

class Authentication(object):
    # sign up new user
    def create_user(self, username, password):
        user = {
            'id': id+ 1,
            'username': username,
            'password': password
        }
        users.append(user)
        return True

    # login user
    def login(self, username, password):
        for user in users:
            if username in dict.values(user):
                pwd = user['password']
                if pwd == password:
                    logged_in = True
                    return True # TODO: replace with json object { logged_in: true, statusCode: 200}
                return False
            return "user doesnt exist"

    def create_bucket_list(self, username, item):
        logged_in = True
        if logged_in:
            bucketlist.append({ 'user': username, 'item': item, 'done': False })
            return True
        else:
            return "please login or sign up to add new bucketlist"

    def update_bucket_list_item(self, username, item, updated_item):
        logged_in = True
        if logged_in:
            for b_item in bucketlist:
                if item in dict.values(b_item):
                    b_item['item'] = updated_item
                    return True
                return False
        else:
            return "please login or sign up to add new bucketlist"

    def delete_bucket_list_item(self, username, item):
        logged_in = True
        print("bucketlist", bucketlist, item)
        if logged_in:
            for b_item in bucketlist:
                if item in dict.values(b_item):
                    bucketlist.remove(b_item)
                    return True
                return "item not found"
        else:
            return "please login or sign up to add new bucketlist"
