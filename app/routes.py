#Imports
import os
from app import myapp_obj
from flask import render_template, redirect, flash, url_for, request, session
from app.forms import LogIn_Form, SignUp_Form, EditProfile_Form, Delete_Form, Search_Form, Post_Form 
from app.models import Like, User, Following, Chirp
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_required, login_user, logout_user
from .functions import get_weather
from sqlalchemy import exc
from app import db
from datetime import date
import uuid

IMAGE_PATH = f"{os.getcwd()}/app/static/images/"

#Home page route
@myapp_obj.route('/home', methods = ['POST', 'GET'])
@myapp_obj.route('/', methods = ['POST', 'GET'])
def home():
    form = Post_Form()
    
    #Checks if user is logged in
    if current_user.is_authenticated:

        #Grabs external weather API
        weather = get_weather()

        #Post Form
        if form.validate_on_submit():
            #Saves input into DB
            chirp = Chirp(text=form.text.data, user_id=current_user.id, date_posted = date.today())
            db.session.add(chirp)
            db.session.commit()
            return redirect('/home')
        
        #Gets all posts from DB
        posts = []
        total = Chirp.query.count()
        if(total>=5):
            for i in range(total, total-5, -1):
                posts.append(Chirp.query.filter_by(id=i).one())
                
        else:
            
            for i in range(total,0,-1):
                posts.append(Chirp.query.filter_by(id=i).one())
        
        #Renders in home.html
        return render_template('home.html', weather=weather, form=form, chirps=posts, User=User, followers=current_user.get_followers())

    #redirects to login page if user is not logged in
    return redirect(url_for('login'))


#Login Page route
@myapp_obj.route("/login", methods=['POST', 'GET'])
def login():
    try:

        #Login form
        form = LogIn_Form()
        if form.validate_on_submit():

            user = User.query.filter_by(username=form.username.data).first()

            #If username and password is incorrect
            if not user or not user.check_password(form.password.data):
                flash('Username or password is not correct!')
                return redirect('/login')
            login_user(user, remember=form.remember_me.data)

            return redirect('/home')
        return render_template('login.html', form=form)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered! Please refresh."

#Sign-up Page route
@myapp_obj.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    try:
        form = SignUp_Form()

        #Sign-up Form
        if form.validate_on_submit():
            hashedPassword = generate_password_hash(form.password.data)
            #Saves Input into DB
            user = User(
                username=form.username.data,
                email=form.email.data, 
                password=hashedPassword,
                profile_icon="default.png")
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        return render_template('sign_up.html', form=form)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered! Please refresh."

#Logout Route
@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#User Profile Route
@myapp_obj.route('/user/<username>', methods=['GET', 'POST'])
def user_profile(username):
    try:
        #Getting Data from Database
        user = User.query.filter_by(username=username).first()
        chirps = Chirp.query.filter_by(user_id=user.id).all()
        
        #User DNE
        if not user:
            flash('This user does not exist')
            return redirect('/')

        #On your own Profile
        if request.method == 'GET':
            return render_template('user_profile.html', user=user, chirps=chirps)

        #On other user profile
        if current_user != user:
            flash("You don't have permission to this resource")
            return render_template('user_profile.html', user=user, chirps=chirps)

        #Edit Form cancel
        form = EditProfile_Form()
        if form.cancel.data:
            return render_template('user_profile.html', user=user, chirps=chirps)

        #Delete User
        if request.form.get("_method") == "DELETE":
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('login'))

        #Edit Form on User profile page
        if request.form.get("_method") == "PUT" and form.validate_on_submit():
            if form.icon.data:
                # generate a unique name for the image
                file = form.icon.data
                extension = file.filename[-4:]
                file.filename = uuid.uuid4().hex
                file.save(f"{IMAGE_PATH}{file.filename}.{extension}")
                user.profile_icon = f"{file.filename}.{extension}"
            user.bio = form.bio.data
            user.nickname = form.nickname.data
            db.session.commit()
            return render_template('user_profile.html', user=user, chirps=chirps)

        return render_template('edit_profile.html', form=form, user=user)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered! Please refresh."

#Edit Page Route
@myapp_obj.route('/user/<username>/edit', methods=['GET', 'POST'])
def edit_profile(username):
    try:
        form = EditProfile_Form()
        
        #Gets data from DB
        user = User.query.filter_by(username=username).first()

        # Check if authenticated user is the same as the user whose profile is being viewed
        if current_user != user:
            flash('You are unauthorized to access this resource')
            return redirect(f'/user/{username}')

        #Gets data from user input
        if request.method == "GET":
            form.bio.data = user.bio
            form.nickname.data = user.nickname

        return render_template('edit_profile.html', form=form, user=user)
    except exc.SQLAlchemyError as err:
        db.session.rollback()
        print(err)
        return "Unexpected error encountered! Please refresh."

#Follower Route
@myapp_obj.route('/follow/<int:id>')
@login_required
def follow(id):
    try:
        if id != current_user.id:  # check it not the user itself
            followee = User.query.filter_by(id=id).one()   
            if not current_user.is_following(id):   # check already followed or not
                new = Following(current_user.id, id)
                db.session.add(new)
                db.session.commit()  # successfully followed  
            return redirect(url_for('user_profile', username=followee.username))
        else:
            return redirect(url_for('user_profile', username=current_user.username))
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return redirect(url_for('home'))

#Unfollower Route
@myapp_obj.route('/unfollow/<int:id>')
@login_required
def unfollow(id):
    try:
        if id != current_user.id:  # check it not the user itself
            followee = User.query.filter_by(id=id).first()   
            if current_user.is_following(id):   # if the user did follow this person
                edge = Following.query.filter_by(followee_id=id, follower_id=current_user.id).first()
                db.session.delete(edge)
                db.session.commit()
            return redirect(url_for('user_profile', username=followee.username))
        else:
            return redirect(url_for('user_profile', username=current_user.username))
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return redirect(url_for('home'))


 

#Delete Profile Route
@myapp_obj.route('/user/<username>/delete', methods=['GET', 'POST'])
def delete(username):
    form = Delete_Form()
    #Switches to delete.html
    if request.method == 'GET':
        return render_template('delete.html', form=form, username=username)

    if form.cancel.data:
        return redirect(url_for('home'))


    if current_user.username != username:
        flash("You don't have permission to this resource")
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if not user.check_password(form.password.data):
            flash('Password is not correct!')
            return render_template('delete.html', form=form, username=username)

        #deletes user from DB
        db.session.delete(user)
        db.session.commit()
        return redirect('/login')

    return redirect(url_for('home'))

# pass stuff to navbar 
@myapp_obj.context_processor
def base():
    form = Search_Form()
    return dict(search_form=form)

#Search Bar Route
@myapp_obj.route('/search', methods=['POST'])
def search():
    form = Search_Form()
    if form.validate_on_submit():
        input = form.input.data
        user = User.query.filter(User.username.like('%' + input + '%'))
        user = user.order_by(User.username).all()
        return render_template('search.html', user=user, form=form)
    
#Dark Mode Route    
@myapp_obj.route("/theme/", methods=['GET'])
def theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    if request.referrer != 'http://127.0.0.1:5000/search':
        return redirect(request.referrer) 
    return redirect('/')

@myapp_obj.route("/chirp/<int:id>/like", methods=["POST"])
@login_required
def likeOrUnlikeChirp(id):
    like = Like.query.filter_by(user_id=current_user.id, chirp_id=id).first()

    back = request.referrer

    if not like:
        # like a chirp
        like = Like(current_user.id, id)
        db.session.add(like)
        db.session.commit()
    else:
        # undo a like
        db.session.delete(like)
        db.session.commit()
    
    return redirect(back)

