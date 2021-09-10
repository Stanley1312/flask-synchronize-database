from flask import Flask
import socketio
from config.config import DevelopmentConfig
import os


def create_app(config_file):
    app = Flask(__name__)
    sio = socketio.Server(logger=True)
    app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

    app.config.from_object(config_file)

    from .models import db
    db.init_app(app)

    with app.app_context(): 

        db.create_all()

    return sio, app


sio, app = create_app(DevelopmentConfig())
from . import views