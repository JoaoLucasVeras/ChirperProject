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
        return f'<User: {self.username}>'

    ''' This function belongs to the class, not to any instance 
        Making it to be a class function so we can access it in the front end,
        without passing it multiple times in the user_profile routes 
    '''
    @classmethod
    def is_following(cls, cur, another):
        followees = db.session.query(Follower.followee).filter_by(follower=cur).all()
        lst = [i[0] for i in followees]
        if another in lst:
            return True
        return False

@login.user_loader
def load_user(username):
    return User.query.get(str(username))


class Follower(db.Model):
    __tablename__ = 'follower'
    __table_args__ = (
        db.PrimaryKeyConstraint('follower', 'followee'),
    )

    follower = db.Column(db.String(45))
    followee = db.Column(db.String(45))
    

    def __init__(self, follower, followee):
        self.follower = follower
        self.followee = followee
        
    def __repr__(self):
        return f'<User {self.follower} is following {self.followee}>'


