from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin
from app import db
from datetime import date, datetime

@login.user_loader
def load_user(username):
    return User.query.get(str(username))

#User DB Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(102))
    email = db.Column(db.String(45), unique=True)
    bio = db.Column(db.String(2000))
    nickname = db.Column(db.String(45))
    profile_icon = db.Column(db.String(45))

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

    def follower_count(self):
        return len(self.get_followers())
    
    def following_count(self):
        return len(self.get_followees())

    def __repr__(self):
        return f'<User: {self.username}>'

    def is_following(self, another):
        lst = self.get_followees()
        return another in lst
    
    def __repr__(self):
        return f'<User: {self.username}>'

#Post "Chirp" DB Model
class Chirp(db.Model):
    __tablename__ = 'chirp'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(2000))
    image_name = db.Column(db.Integer) #look into
    date_posted = db.Column(db.Date)

    def getLikes(self):
        likes = db.session.query(Like.user_id).filter_by(chirp_id=self.id).all()
        res = [like[0] for like in likes]
        return res

#Following DB Model
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

# Like Model
class Like(db.Model):
    __tablename__ = "like"
    __table_args__ = (
        db.PrimaryKeyConstraint('user_id', 'chirp_id'),
    )

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chirp_id = db.Column(db.Integer, db.ForeignKey('chirp.id'))

    def __init__(self, user_id, chirp_id):
        self.user_id = user_id
        self.chirp_id = chirp_id
        
    def __repr__(self):
        return f'<User #{self.user_id} liked chirp #{self.chirp_id}>'


