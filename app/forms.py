from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LogIn_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class SignUp_Form(FlaskForm):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    username = StringField('username')
    email = StringField('email')
    password = PasswordField('password')
    cofirm_password = PasswordField('Confirm Password')

    submit = SubmitField('sign up')