import socketio
from flask import Flask
from config.config import DevelopmentConfig
import os

sio = socketio.Client()

def create_app(config_file):
    app = Flask(__name__)

    app.config.from_object(config_file)

    from .models import db
    db.init_app(app)

    with app.app_context(): 

        db.create_all()

    return app

app = create_app(DevelopmentConfig())
from . import views