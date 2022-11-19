from app import myapp_obj
from flask import render_template, redirect, flash, url_for
from app.forms import LogIn_Form, SignUp_Form
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from app import db

#plan out routes we are going to need

@myapp_obj.route('/home')
def home():
    return render_template("home.html")


@myapp_obj.route("/login", methods=['POST', 'GET'])
def login():
    form = LogIn_Form()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.username.data).first()
    
        if not user or not user.check_password(form.password.data):
            flash('Username or password is not correct!')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)

        return redirect('/home')
    return render_template('login.html', form=form)


@myapp_obj.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    form = SignUp_Form()
    if form.validate_on_submit():
        hashedPassword = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashedPassword)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('sign_up.html', form=form)


@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@myapp_obj.route('/user-profile', methods = ['POST', 'GET'])
def user_profile():
    return render_template('user_profile.html')

