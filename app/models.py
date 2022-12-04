from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(102))
    email = db.Column(db.String(45), unique=True)
    bio = db.Column(db.String(2000))
    nickname = db.Column(db.String(45))


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Chirp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    text = db.Column(db.String(2000))
    image_name = db.Column(db.Integer) #look into
    likes = db.Column(db.Integer)
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

