## Building Url Dynamically 
## variable rule 
## Jinja  template Engine

## Jinga 2 template engine 

'''
{{ }} expressions to print output in html 

{%,,,%} condtionals , for loop
{#.....#} this is for comments 

'''

from flask import Flask, render_template, request
'''
It creates an instance of the Flask class, 
which will be our WSGI(Web Sever Gateway Interface) application

We have intialized the flsk 
'''
## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html>H1>Welconme to the flask playground"

@app.route("/index", methods =['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method== 'POST':
        name = request.form["name"]
        return f"Hello {name}"

    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method== 'POST':
        name = request.form["name"]
        return f"Hello {name}"

    return render_template('form.html')

# Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res= ""
    if score>= 50:
        res= "PASS"

    else:
        res = "FAIL"
        
    exp = {'score:':score, "res":res}

    return render_template('result1.html', results = exp)


## Building URL dynamically 



# this is the entry point of our flask / app
if __name__ == "__main__":
    app.run(debug= True) 
# agat ham koi bhi change krte h code me toh
# ye direcr server ko restart kr dega aur local host me changes dikhege