from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_object(Config)

# update(
#     SECRET_KEY='this-is-a-secret',
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
# )
db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models




