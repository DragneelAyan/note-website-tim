from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters', category='error')
        elif password1 != password2:
            flash('Invalid password', category='error')
        else:
            flash('Account created!', category='success')
        
    return render_template("signup.html")