from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

myapp_obj = Flask(__name__)
CSRFProtect(myapp_obj)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_object(Config)

db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models




