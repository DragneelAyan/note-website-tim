from flask import Blueprint, render_template
#This basically defines that this file is the blueprint of our application, 
# it has all the required routes defined here. 


views = Blueprint('views', __name__)

#Now we write '@' then the name of our blueprint, and then '.route' and 
# inside bracket we give the route
@views.route('/') 
def home(): #this function will run whenever we go to the above route 
    return render_template("home.html")