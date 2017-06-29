import string
import random

from flask import Flask
from controllers.accounts_manager import AccountsManager
from controllers.bucketlist import BucketList
from controllers.bucketlist_items import BucketListItems


# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = ''.join([random.choice(string.ascii_letters + string.digits)
                          for n in range(15)])

# app controllers
accounts_manager = AccountsManager()
bucket_list = BucketList()
bucket_list_items = BucketListItems()

from app import views

# Load the config file
app.config.from_object('config')
