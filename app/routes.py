from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LogIn_Form, SignUp_Form
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from app import db

#plan out routes we are going to need
@myapp_obj.route("/login", methods=['POST', 'GET'])
def login():
    form = LogIn_Form()
    if form.validate_on_submit():
        print('valid')
        user = User.query.filter_by(username=form.username.data).first()
    
        if not user or not user.check_password(form.password.data):
            flash('Wrong password!')
            return redirect('/login')

        login_user(user, remember=form.remember_me.data)
        flash('Login Successfully')
        return redirect('/')
    return render_template('login.html', form=form)


@myapp_obj.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    form = SignUp_Form()
    if form.validate_on_submit():
        print("no?")
        hashedPassword = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashedPassword)
        db.session.add(user)
        db.session.commit()
        flash("Register Successfully")
        print("SUCCESS!!")
        return redirect('/')
    
    return render_template('sign_up.html', form=form)