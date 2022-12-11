from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from .models import User


class LogIn_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class SignUp_Form(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[
        DataRequired(), Length(min=8, max=50),
        EqualTo('confirm_password', message='Should match to the password')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])

    submit = SubmitField('sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Please try a new one!!!')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. Please try a new one!!!')

# Form for editing user profile info
class EditProfile_Form(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    icon = FileField('Icon', validators=[FileAllowed(['jpg', 'png'], "Only .png or .jpg files allowed!")])
    cancel = SubmitField('Cancel')
    submit = SubmitField('Save Profile')

class Delete_Form(FlaskForm):
    password = PasswordField('Password')
    cancel = SubmitField('Cancel')
    submit = SubmitField('Confirm')


class Search_Form(FlaskForm):
    input = StringField('Searched', validators=[DataRequired()])
    search = SubmitField('Search')

class Post_Form(FlaskForm):
    text = TextAreaField('Message', validators=[DataRequired()])
    #image
    submit = SubmitField('Post')
    cancel = SubmitField('Cancel')