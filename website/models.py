from . import db #Here what we are doing is, we are importing from the current package the db object.
# In '__init__.py' we have db defined. We are importing from '__init__.py', so we are importing
# from the 'website' package.
from flask_login import UserMixin #This is just a custom class that we can inherit that will give 
#our user object things specific for our user login. 'flask_login' is just a module that helps us log 
# user in. And user object needs to inherit from our 'UserMixin' which is what we are importing here.
from sqlalchemy.sql import func


class User(db.Model, UserMixin): #Here we define our class and inherit 'db.Model'. 'db.Model' is the 
#   sqlalchemy object we created. A database model is a schema or layout for a object that's going 
# to be stored in our database.
#   Now we are defining our schema or layout that is going to be stored in the database
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    notes = db.relationship('Note')
    

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #'timezone=True' this is going 
#   to store timezone info as well. We imported func from sqlalchemy and 'default=func.now()': what 
#   we did is whenever we create a new note, sqlalchemy will automatically add the date.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
    