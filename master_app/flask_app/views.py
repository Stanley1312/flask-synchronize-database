from flask_app import app, sio
from flask import request
from .models import db, User
from .utils import get_all_users
import sqlalchemy


# =============================================================================


@app.route("/user", methods=["GET"])
def get_all_user():

    if request.method == "POST":
        return "Not allowed method", 400 

    result = get_all_users()
    return {
            "master_app" :
                {
                "list_users" : result
                }
            }

@app.route("/user", methods=["POST"])
def insert_user():

    if request.method == "GET":
        return "Not allowed method", 400

    data = request.get_json()
    username = data.get("username")
    email = data.get('email')

    print(username, email)

    user = User(username=username, email=email)
    try:
        db.session.add(user)
        db.session.commit()    
    except Exception as e:
        print(e)
        db.session.rollback()
        return '', 204

    return user.to_dict()

@app.route("/user/<string:id>", methods=['DELETE'])
def delete_user(id):

    if request.method != 'DELETE':
        return "Not allowed method", 400
    
    user = User.query.filter_by(id=id).delete()
    db.session.commit()

    return 'Delete successfull'
    

@app.route("/sync", methods=["POST"])
def sync_user():

    if request.method == "POST":
        return "Not allowed method", 400
    
    # get all current users
    current_users = User.query.all()
    set_usernames = set(map(lambda x:x.username, current_users))
    print(set_usernames)
    
    data = request.get_json()
    list_users = data.get('list_users')

    new_users = []

    for user in list_users:
        if user["username"] not in set_usernames:
            add_user = User(username=user["username"], email=user["email"])
            new_users.append(user)
            try:
                db.session.add(add_user)
                db.session.commit()
            except Exception as e:
                print(e)
                return '', 204
    return {
        'new_users': new_users
    }

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.emit('my_response', {'data': 'Connected', 'count': 0})


@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)