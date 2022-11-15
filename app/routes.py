from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

#plan out routes we are going to need
