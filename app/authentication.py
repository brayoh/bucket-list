"""
    Handle User Authentication and Registration
"""
ID = 0


class Authentication(object):
    """ docstring for Authentication """

    def __init__(self):
        self.users = [{'id': 0, 'username': 'john', 'password': 'doe'}]

    """ signup new user
        parameters: username, password
    """
    def signup(self, username, password):
        user = {
            'id': ID + 1,
            'username': username,
            'password': password
        }

        total_users = len(self.users)
        self.users.append(user)

        # check if user object has incremented to be sure that user was added
        return True if total_users < len(self.users) else False

    """
        login existing user
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
