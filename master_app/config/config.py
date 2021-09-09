from os import environ as env
import os
from dotenv import load_dotenv
load_dotenv()


class Config():
    TESTING = False

class DevelopmentConfig(Config):
    DB_PATH = f'{os.getcwd()}/db'
    DB_NAME = 'test.db'
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI', f'sqlite:///{DB_PATH}/{DB_NAME}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
