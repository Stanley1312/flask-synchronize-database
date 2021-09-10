from flask_app import app
from .models import db, User
from flask import request

@app.route("/")
def get_all_user():
    query = User.query.all()
    result = list(map(lambda x: x.to_dict(), query))
    
    return {
            "sub_app_a" :
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