from app import myapp_obj
from flask import render_template, redirect, flash, url_for, request
from app.forms import LogIn_Form, SignUp_Form, EditProfile_Form
from app.models import User
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import exc

from app import db

#plan out routes we are going to need

@myapp_obj.route('/home')
@myapp_obj.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html')

    return redirect(url_for('login'))


@myapp_obj.route("/login", methods=['POST', 'GET'])
def login():
    try:
        form = LogIn_Form()
        if form.validate_on_submit():
            
            user = User.query.filter_by(username=form.username.data).first()
        
            if not user or not user.check_password(form.password.data):
                flash('Username or password is not correct!')
                return redirect('/login')
            login_user(user, remember=form.remember_me.data)

            return redirect('/home')
        return render_template('login.html', form=form)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered"

@myapp_obj.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    try:
        form = SignUp_Form()
        if form.validate_on_submit():
            hashedPassword = generate_password_hash(form.password.data)
            user = User(username=form.username.data, email=form.email.data, password=hashedPassword)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        return render_template('sign_up.html', form=form)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered"


@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@myapp_obj.route('/user/<username>', methods = ['GET', 'POST'])
def user_profile(username):
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('This user does not exist')
            return redirect('/')
        
        if request.method == 'GET':
            return render_template('user_profile.html', user=user)
        
        if current_user != user:
            flash("You don't have permission to this resource")
            return render_template('user_profile.html', user=user)
        

        form = EditProfile_Form()
        if form.cancel.data:
            return render_template('user_profile.html', user=user)
        
        if request.form.get("_method") == "DELETE":
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('login'))

        if request.form.get("_method") == "PUT" and form.validate_on_submit():
            user.bio = form.bio.data
            user.nickname = form.nickname.data
            db.session.commit()
            return render_template('user_profile.html', user=user)

        return render_template('edit_profile.html', form=form, user=user)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered"

@myapp_obj.route('/user/<username>/edit', methods = ['GET', 'POST'])
def edit_profile(username):
    try:
        form = EditProfile_Form()
        user = User.query.filter_by(username=username).first()
        
        # Check if authenticated user is the same as the user whose profile is being viewed
        if current_user != user:
            flash('You are unauthorized to access this resource')
            return redirect(f'/user/{username}')
        
        if request.method == "GET":
            form.bio.data = user.bio
            form.nickname.data = user.nickname

        return render_template('edit_profile.html', form=form, user=user)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered"


