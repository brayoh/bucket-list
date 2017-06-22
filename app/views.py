from flask import (render_template, request, jsonify, session, abort,
                   redirect, url_for)

from app import (app, accounts_manager, bucket_list, bucket_list_items)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        if all(key in request.form for key in ("username", "password")):
            username = request.form['username'].strip()
            password = request.form['password'].strip()
            if all(len(value) > 0 for value in [username, password]):
                user = accounts_manager.signup(username, password)
                response = {"status": "success",
                            "message": "user was registered successfully"
                            }
            else:
                response = {"status": "failed",
                            "message": """please enter a valid username
                                       or password to continue"""
                            }
            return render_template("signup.html", response=response)
        else:
            response = {"status": "failed",
                        "message": """please enter a valid username or
                                   password to continue"""
                        }
            return render_template("signup.html", response=response)
    else:
        return render_template("signup.html", response="")


@app.route('/login', methods=['GET', 'POST'])
def login():
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
                                "message": """username or password is
                                           incorrect"""
                                }
                    return render_template("login.html",
                                           response=response)
            else:
                response = {"status": "failed",
                            "message": """please enter a valid username
                                        or password to continue"""
                            }
                return render_template("login.html",
                                       response=response)
        else:
            response = {"status": "failed",
                        "message": """please enter a valid username or
                                   password to continue"""
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
        if method == "POST":
            if all(key in request.form for key in ("name", "description")):
                name = request.form['name'].strip()
                description = request.form['description'].strip()
                new_bucketlist = bucket_list.create_bucket_list(user_id,
                                                                name,
                                                                description)
                bucketlists = bucket_list.get_user_bucketlists(user_id)
                response = {"status": "success",
                            "message": "bucketlist created successfully"
                            }
                return render_template("dashboard.html",
                                       data={'username': username,
                                             'bucketlist': bucketlists,
                                             'response': response})
            else:
                response = {"status": "failed",
                            "message": """please add details to
                            create a new bucketlist"""}
                bucketlists = bucket_list.get_user_bucketlists(user_id)

                return render_template("dashboard.html",
                                       data={'username': username,
                                             'bucketlist': bucketlists,
                                             'response': response})

        elif method == "GET":
                # get all bucketlists with user_id for logged in user
                bucketlists = bucket_list.get_user_bucketlists(user_id)
                print(bucketlists)
                return render_template("dashboard.html",
                                       data={'username': username,
                                             'bucketlist': bucketlists,
                                             'response': ""})
        else:
            abort(401)
    else:
        return redirect(url_for('login'))


@app.route('/bucketlist/<id>', methods=['GET', 'POST'])
def single_bucketlist(id):
    if 'username' in session:
        username = session['username']
        user_id = int(accounts_manager.get_user_id(username))
        bucketlist = bucket_list.get_bucketlist_by_id(user_id, int(id))
        if request.method == "GET":
            if all(key in request.args for key in ("name", "description")):
                name = request.args['name']
                description = request.args['description']
                update = bucket_list.update_bucket_list(int(id),
                                                        name,
                                                        description)
                if update:
                    return render_template("bucketlist.html",
                                           data={"bucketlist": bucketlist,
                                                 "response": ""})
                else:
                    return render_template("bucketlist.html",
                                           data={"bucketlist": bucketlist,
                                                 "response": "update failed"})
        return render_template("bucketlist.html",
                               data={"bucketlist": bucketlist,
                                     "response": ""})
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))
