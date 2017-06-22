from datetime import datetime
id = 0


class AccountsManager(object):
    """ This class handles user authentication and registration """
    def __init__(self):
        self.users = []

    def signup(self, username, password):
        """add a new user to the db
        parameters: username, password
        """
        if len(self.users) > 0:
            user_id = (self.users[len(self.users)-1]['id'] + 1)
        else:
            user_id = id + 1
        user = {
            'id': user_id,
            'username': username,
            'password': password,
            'created_at': datetime.utcnow().isoformat()
        }
        total_users = len(self.users)

        if self.get_user_id(username):
            return False
        else:
            self.users.append(user)

        # check if user list has incremented to be sure that user was added
        return True if total_users < len(self.users) else False

    def login(self, username, password):
        """login an existing user
        parameters: username, password
        """
        for user in self.users:
            if username in dict.values(user):
                if password == user['password']:
                    return True
                else:
                    break  # password is wrong break out of the loop
        else:
            return False

    def get_user_id(self, username):
        """find a user in our users list and return the id
        parameters: username
        """
        for user in self.users:
            if user['username'] == username:
                return user['id']
                break
        else:
            return None
