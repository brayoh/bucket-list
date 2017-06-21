from flask import (render_template, request, jsonify, session, abort)

from app import (app, accounts_manager, bucket_list, bucket_list_items)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        if 'username' and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            user = accounts_manager.signup(username, password)
            return jsonify({"status": "success","message":"user was registered successfully"})
        else:
            return jsonify({"status":"failed", "message":"username and password should be included in request body"})
    else:
        return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    users = accounts_manager.users
    if request.method == "POST":
        if 'username' and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            login_user = accounts_manager.login(username, password)
            if login_user:
                session['username'] = username
                return jsonify({"status": "success","message":"user login was successful"})
            else:
                return jsonify({"status": "failed","message":"username or password is incorrect"})
        else:
            return jsonify({"status":"failed", "message":"username and password should be included in request body"})
    return render_template("login.html")


@app.route('/bucketlists')
def get_all_bucketlists():
    pass

""" This method will handle all bucketlist activities (create, edit, update, delete)
        USAGE:
    POST request:{
        "name": name of bucketlist
        "description": description of bucketlist
    }
    for get you use either name or id
    GET request:{
        "id": bucketlist id
        "name":  bucketlist name
    }
    PUT request:{
        "id":  bucketlist id
        "type": name/description
        "update_value": value to update with
    }

    DELETE request:{
        "id":  bucketlist id
    }

"""

@app.route('/bucketlist', methods=['GET','POST','PUT','DELETE'])
def bucketlist():
    method = request.method
    if 'username' in session:
        username = session['username']
        user_id = accounts_manager.get_user_id(username)

        if method == "POST":
            if all(key in request.form for key in ("name","description")):
                name = request.form['name']
                description = request.form['description']
                new_bucketlist = bucket_list.create_bucket_list(user_id, name, description)
                return jsonify({ "bucketlist": new_bucketlist[1], "status":"success", "message":"bucketlist created successfully"})
            else:
                return jsonify({"status":"failed", "message":"name and description should be included in request body"})
        elif method == "GET":
            if 'id' in request.args:
                # since user is logged in, we get all bucketlists with user_id for user
                bucketlists = bucket_list.get_user_bucketlists(user_id)
                return jsonify({"bucketlists": bucketlists})
            else:
                return jsonify({"status":"failed", "message":"bucketlist id should be included in request body"})
        elif method == "PUT":
            if all(key in request.form for key in ("id","type","update_value")):
                bucketlist_id = request.form['id']
                update_type = request.form['type']
                update_value = request.form['update_value']

                if bucket_list.check_bucketlist_exists(bucketlist_id):
                    update = bucket_list.update_bucket_list(update_type, update_value)
                    if update[0] == True:
                        return jsonify({"bucketlists": update[1]})
                    else:
                        return jsonify({"status":"failed", "message":"bucketlist not found"})
                else:
                    return jsonify({"status":"failed", "message":"bucketlist not found"})
            else:
                return jsonify({"status":"failed", "message":"id, type, update_value should be included in request body"})
        elif method == "DELETE":
            if 'id' in request.args:
                if bucket_list.delete_bucket_list(request.args['id']):
                    return jsonify({"status":"success", "message":"bucketlist successfully deleted"})
            else:
                return jsonify({"status":"failed", "message":"id should be included in request body"})
        else:
            abort(401)
    else:
        return jsonify({"status":"failed", "message":"please login or signup or access your bucketlist"})



@app.route('/items',     methods=['GET','POST','PUT','DELETE'])
def bucketlistitems():
    method = request.method
    if 'username' in session:
        username = session['username']
        user_id = accounts_manager.get_user_id(username)
        bucketlist_id = request.form['id']

        if bucket_list.check_bucketlist_exists(bucketlist_id):
            if method == "POST":
                print(request.form['name'])
                if 'name' and 'id' in request.form:
                    name = request.form['name']
                    new_item = bucket_list_items.create_item(bucketlist_id, name)
                    return jsonify({ "item": new_item[1], "status":"success", "message":"bucketlist item added successfully"})
                else:
                    return jsonify({"status":"failed", "message":"name and description should be included in request body"})
            elif method == "GET":
                if 'id' in request.form:
                    # since user is logged in, we get all items with user_id for user
                    item = bucket_list.get_item_by_id(request.form['id'])
                    return jsonify({"item": item})
                else:
                    return jsonify({"status":"failed", "message":"bucketlist id should be included in request body"})
            elif method == "PUT":
                if all(key in request.form for key in ("id","type","update_value")):
                    bucketlist_id = request.form['id']
                    update_type = request.form['type']
                    update_value = request.form['update_value']

                    if bucket_list.check_bucketlist_exists(bucketlist_id):
                        update = bucket_list.update_bucket_list(update_type, update_value)
                        if update[0] == True:
                            return jsonify({"bucketlists": update[1]})
                        else:
                            return jsonify({"status":"failed", "message":"bucketlist not found"})
                    else:
                        return jsonify({"status":"failed", "message":"bucketlist not found"})
                else:
                    return jsonify({"status":"failed", "message":"id, type, update_value should be included in request body"})
            elif method == "DELETE":
                if 'id' in request.args:
                    if bucket_list.delete_item(request.args['id']):
                        return jsonify({"status":"success", "message":"bucketlist successfully deleted"})
                else:
                    return jsonify({"status":"failed", "message":"id should be included in request body"})
            else:
                abort(401)
        else:
            return jsonify({"status":"failed", "message":"bucketlist not found"})
    else:
        return jsonify({"status":"failed", "message":"please login or signup or access your bucketlist"})


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
