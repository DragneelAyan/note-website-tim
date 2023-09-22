#by creating the init.py file in the website folder, we can use that folder as a python package
from website import create_app 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#app.run is going to run our Flask application and start our web server, and 'debug=True' means 
#every time we make a change in the application, it is going to restart our web server. 
 ## So we completed creating our web server. 