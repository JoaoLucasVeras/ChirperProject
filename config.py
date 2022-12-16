from dotenv import load_dotenv
import os

#Looks into .env File
load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
#Getting DB Info
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DB_CONNECTION = os.environ.get("DB_CONNECTION")
    # DB_USER = os.environ.get("DB_USER")
    # DB_PASSWORD = os.environ.get("DB_PASSWORD")
    # DB_PORT = os.environ.get("DB_PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")