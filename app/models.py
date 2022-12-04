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


    def get_followees(self):
        all = db.session.query(Following.followee_id).filter_by(follower_id=self.id).all()
        lst = [i[0] for i in all]
        return lst
    
    def get_followers(self):
        all = db.session.query(Following.follower_id).filter_by(followee_id=self.id).all()
        lst = [i[0] for i in all]
        return lst

    def __repr__(self):
        return f'<User {self.username}>'

class Chirp(db.Model):
    __tablename__ = 'chirp'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', 'user_id', 'text', 'image_name', 'likes'),
    )

    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(2000))
    image_name = db.Column(db.Integer) #look into
    likes = db.Column(db.Integer)
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Following(db.Model):
    __tablename__ = 'following'
    __table_args__ = (
        db.PrimaryKeyConstraint('follower_id', 'followee_id'),
    )

    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    

    def __init__(self, follower_id, followee_id):
        self.follower_id = follower_id
        self.followee_id = followee_id
        
    def __repr__(self):
        return f'<User #{self.follower_id} is following #{self.followee_id}>'