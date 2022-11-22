from flask_wtf import FlaskForm
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
    cancel = SubmitField('Cancel')
    submit = SubmitField('Save Profile')
