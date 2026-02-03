from flask import Flask 
'''
It creates an instance of the Flask class, 
which will be our WSGI(Web Sever Gateway Interface) application

We have intialized the flsk 
'''
## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best flask playground. This should be a amazing cource"

@app.route("/index")
def index():
    return "Welcome to this index page "

# this is the entry point of our flask / app
if __name__ == "__main__":
    app.run(debug= True) # agat ham koi bhi change krte h code me toh ye direcr server ko restart kr dega aur local host me changes dikhege