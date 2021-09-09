from flask_app import app
from .models import db, User
from flask import request

@app.route("/")
def get_all_user():
    query = User.query.all()
    result = list(map(lambda x: x.to_dict(), query))
    
    return {
        "list_users" : result
    }

