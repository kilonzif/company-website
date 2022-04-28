from flask import render_template
from app import app

# Views UI 

# @app.route("/")
# def home():
#     pageName = "Home"
#     return render_template("home.html",pageName=pageName)


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('website.html')

@app.route("/about")
def aboutUs():
    message = "Our Vision Goes Here"
    return render_template('about.html',message=message)

