from datetime import datetime
id = 0


class AccountsManager(object):
    """ This class handles user authentication and registration """
    def __init__(self):
        self.users = []

    """ add a new user to the db
        parameters: username, password
    """
    def signup(self, username, password):
        user_id = (self.users[len(self.users)-1]['id'] + 1) if len(self.users) > 0 else id + 1
        user = {
            'id': user_id,
            'username': username,
            'password': password,
            'created_at': datetime.utcnow().isoformat()
        }

        total_users = len(self.users)
        self.users.append(user)

        # check if user list has incremented to be sure that user was added
        return True if total_users < len(self.users) else False

    """
        login an existing user
        parameters: username, password
    """
    def login(self, username, password):
        for user in self.users:
            if username in dict.values(user):
                if password == user['password']:
                    return True
                else:
                    break  # password is wrong break out of the loop
        else:
            return False

    """ find a user in our users list and return the id
        parameters: username
    """
    def get_user_id(self, username):
        for user in self.users:
            if username in dict.values(user):
                return user['id']
            else:
                return None
