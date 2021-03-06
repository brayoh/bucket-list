import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class AccountsManager(object):
    """ This class handles user authentication and registration """
    def __init__(self):
        self.users = []
        self.id = 0

    def signup(self, username, password):
        """add a new user to the db
        parameters: username, password
        """
        if len(self.users) > 0:
            user_id = (self.users[len(self.users)-1]['id'] + 1)
        else:
            user_id = self.id + 1

        user = { 'id': user_id, 'username': username, 'password': password,
                'created_at': datetime.utcnow().isoformat()
        }

        if self.check_user_exists(username):
            return False
        else:
            total_users = len(self.users)
            self.users.append(user)
            logger.error("users list {}".format(self.users))

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
            return False

    def check_user_exists(self, username):
        """find a user in our users list
        parameters: username
        """
        for user in self.users:
            if user['username'] == str(username):
                return True
                break
        else:
            return False
