from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST': #As we are loggin in, we are givving data to web server, hence - 'POST'.
        email = request.form.get('email') #We want email and password from the form.
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first() #Now we check if we have the typed in user email 
        #in our database
        if user:
            if check_password_hash(user.password, password): #We check if the typed in password is same 
                #with the one saved in database
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home')) #Opens the home page
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('Email does not exist!', category='error')    
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters', category='error')
        elif password1 != password2:
            flash('Invalid password', category='error')
        else:
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user=current_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        
    return render_template("signup.html", user=current_user)