from flask import Flask
from flask_socketio import SocketIO
from config.config import DevelopmentConfig
import os

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)

    from .models import db
    db.init_app(app)

    with app.app_context(): 

        db.create_all()
    
    socketio = SocketIO(app, cors_allowed_origins="*")

    return socketio, app


socketio, app = create_app(DevelopmentConfig())
from . import views