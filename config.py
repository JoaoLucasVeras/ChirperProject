from dotenv import load_dotenv
import os

#Looks into .env File
load_dotenv()

#Getting DB Info
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://'+os.environ.get("DB_CONNECTION")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DB_CONNECTION = os.environ.get("DB_CONNECTION")
    # DB_USER = os.environ.get("DB_USER")
    # DB_PASSWORD = os.environ.get("DB_PASSWORD")
    # DB_PORT = os.environ.get("DB_PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")