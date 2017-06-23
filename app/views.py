from flask import (render_template, request, jsonify, session, abort,
                   redirect, url_for)

from app import (app, accounts_manager, bucket_list, bucket_list_items)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ This method will handle user signup
    parameters: username, password
    """
    if request.method == "POST":
        if all(key in request.form for key in ("username", "password")):
            username = request.form['username'].strip()
            password = request.form['password'].strip()
            if all(len(value) > 0 for value in [username, password]):
                user = accounts_manager.signup(username, password)
                if user:
                    response = {"status": "success",
                                "message": "user was registered successfully"
                                }
                else:
                    response = {"status": "failed",
                                "message": "username is already taken"
                                }
            else:
                response = {"status": "failed",
                            "message": ("please enter a valid username "
                                        "or password to continue")
                            }
            return render_template("signup.html", response=response)
        else:
            response = {"status": "failed",
                        "message": ("please enter a valid username or "
                                    "password to continue")
                        }
            return render_template("signup.html", response=response)
    else:
        return render_template("signup.html", response="")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ This method will handle user login
    parameters: username, password
    """
    users = accounts_manager.users
    if request.method == "POST":
        if all(key in request.form for key in ("username", "password")):
            username = request.form['username'].strip()
            password = request.form['password'].strip()
            if all(len(value) > 0 for value in [username, password]):
                login_user = accounts_manager.login(username, password)
                if login_user:
                    session['username'] = username
                    return redirect(url_for('dashboard'))
                else:
                    response = {"status": "failed",
                                "message": ("username or password is "
                                            "incorrect")
                                }
                    return render_template("login.html",
                                           response=response)
            else:
                response = {"status": "failed",
                            "message": ("please enter a valid username "
                                        "or password to continue")
                            }
                return render_template("login.html",
                                       response=response)
        else:
            response = {"status": "failed",
                        "message": ("please enter a valid username or "
                                    "password to continue")
                        }
            return render_template("login.html", response=response)
    else:
        return render_template("login.html", response="")


@app.route('/dashboard', methods=['GET', 'POST', 'PUT', 'DELETE'])
def dashboard():
    """ This method will handle all bucketlist activities
    """
    method = request.method
    if 'username' in session:
        username = session['username']
        user_id = accounts_manager.get_user_id(username)
        bucketlists = bucket_list.get_user_bucketlists(user_id)
        if method == "POST":
            if all(key in request.form for key in ("name", "description")):
                name = request.form['name'].strip()
                description = request.form['description'].strip()
                if name and description:
                    blist = bucket_list.create_bucket_list(user_id, name,
                                                           description)
                    if blist:
                        bucketlists = bucket_list.get_user_bucketlists(user_id)
                        response = {"status": "success",
                                    "message": ("bucketlist created "
                                                " successfully")}
                        return render_template("dashboard.html",
                                               data={'username': username,
                                                     'bucketlist': bucketlists,
                                                     'response': response})
                    else:
                        response = {"status": "failed",
                                    "message": ("bucketlist with a similar"
                                                " name already exists")}
                        return render_template("dashboard.html",
                                               data={'username': username,
                                                     'bucketlist': bucketlists,
                                                     'response': response})
                else:
                    response = {"status": "failed",
                                "message": ("please add details to "
                                            "create a new bucketlist")}
                    return render_template("dashboard.html",
                                           data={'username': username,
                                                 'bucketlist': bucketlists,
                                                 'response': response})
            else:
                response = {"status": "failed",
                            "message": ("please add details to "
                                        "create a new bucketlist")}

                return render_template("dashboard.html",
                                       data={'username': username,
                                             'bucketlist': bucketlists,
                                             'response': response})

        elif method == "GET":
            if 'delete' in request.args:
                bucketlist_id = request.args['delete']
                delete_blist = bucket_list.delete_bucket_list(bucketlist_id)
                if delete_blist:
                    return redirect(url_for("dashboard"))
                else:
                    response = {"status": "failed",
                                "message": "bucketlist not found"}
                    return render_template("dashboard.html",
                                           data={'username': username,
                                                 'bucketlist': bucketlists,
                                                 'response': ""})

            elif all(key in request.args for key in ("name", "description")):
                name = request.args['name']
                description = request.args['description']
                bucketlist_id = request.args['bucketlist_id']
                update = bucket_list.update_bucket_list(int(bucketlist_id),
                                                        name,
                                                        description)
                if update:
                    return redirect(url_for("dashboard"))
                else:
                    response = {"status": "failed",
                                "message": "bucketlist not found"}

                    return render_template("dashboard.html",
                                           data={'username': username,
                                                 'bucketlist': bucketlists,
                                                 "response": response})
            return render_template("dashboard.html",
                                   data={'username': username,
                                         'bucketlist': bucketlists,
                                         'response': ""})
    else:
        return redirect(url_for('login'))


@app.route('/bucketlist/<id>', methods=['GET', 'POST'])
def single_bucketlist(id):
    if 'username' in session:
        username = session['username']
        user_id = int(accounts_manager.get_user_id(username))
        bucketlist = bucket_list.get_bucketlist_by_id(user_id, int(id))
        items = bucket_list_items.get_item_by_bucketlist_id(int(id))

        if request.method == "GET":
            if all(key in request.args for key in ("activity_name",
                                                   "activity_id")):
                name = request.args['activity_name']
                activity_id = request.args['activity_id']
                activity_status = ""
                if request.args['activity_status'] != '':
                    status = {
                        "on": "done",
                        "off": "not done",
                    }
                    activity_status = status[request.args['activity_status']]
                if any(value == '' for value in['id', 'activity_id']):
                    return render_template("bucketlist_items.html",
                                           data={"bucketlist": bucketlist,
                                                 "activities": items,
                                                 "error":
                                                 "invalid data provided"})
                update_item = bucket_list_items.update_item(activity_id,
                                                            name,
                                                            activity_status)
                if update_item:
                    return render_template("bucketlist_items.html",
                                           data={"bucketlist": bucketlist,
                                                 "activities": items,
                                                 "error": ""})
                else:
                    return render_template("bucketlist_items.html",
                                           data={"bucketlist": bucketlist,
                                                 "activities": items,
                                                 "error": "item not found"})

            elif 'delete' in request.args:
                item_id = int(request.args['delete'])
                delete_item = bucket_list_items.delete_item(item_id)
                items = bucket_list_items.get_item_by_bucketlist_id(int(id))

                if delete_item:
                    url = "/bucketlist/{}".format(id)
                    return redirect(url)
                else:
                    return render_template("bucketlist_items.html",
                                           data={"bucketlist": bucketlist,
                                                 "activities": items,
                                                 "error": ("activity"
                                                           "not found")})
            return render_template("bucketlist_items.html",
                                   data={"bucketlist": bucketlist,
                                         "activities": items,
                                         "error": ""})
        elif request.method == "POST":
                name = request.form['activity_name']
                if name != '':
                    item = bucket_list_items.create_item(int(id), name)
                    if item:
                        items = bucket_list_items.get_item_by_bucketlist_id(id)
                        return render_template("bucketlist_items.html",
                                               data={"bucketlist": bucketlist,
                                                     "activities": items,
                                                     "error": ""})
                    else:
                        response = {"status": "failed",
                                    "message": ("activity already exists"
                                                " please choose a"
                                                "different name")}
                        return render_template("bucketlist_items.html",
                                               data={"bucketlist": bucketlist,
                                                     "activities": items,
                                                     "error": response})

                else:
                    return render_template("bucketlist_items.html",
                                           data={"bucketlist": bucketlist,
                                                 "activities": items,
                                                 "error": ""})
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))
