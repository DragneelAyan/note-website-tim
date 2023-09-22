from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() #Here we are defining the database
DB_NAME = "database.db" #Giving our database a name

def create_app(): #define a function 
    app = Flask(__name__) #initialize our app, this is how we initialize Flask. 
    app.config['SECRET_KEY'] = 'hola_amigo_esta_es_la_clave_secreta'
    #encrypt or secure the cookies and session data on our website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #We are storing the database with this in 'website' folder
    db.init_app(app)
    #Initialize our database with our FLASK app
    
    #here we import our blueprint from our '.views' and '.auth' py files. 
    from .views import views
    from .auth import auth
    
    #Now we register our blueprints with our flask application.
    #the 'url_prefix' addresses 
    #the URLs stored inside the blueprints, and how to access them.
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    #create_database(app)
    #with app.app_context():
    #    db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app #just returns our function

def create_database(app): #This is going to check if the database exists, if it does not then
    if not path.exists('website/' + DB_NAME): # it is going to be created
        db.create_all(app=app)
        print('Created Database!')