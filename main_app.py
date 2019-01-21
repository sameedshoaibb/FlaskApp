#!/usr/bin/python

#To run flask app with environment variable
#export set FLASK_APP=main_app.py
#export set FLASK_DEBUG=1
#flask run

from flask import Flask, render_template, url_for
app = Flask(__name__) #initialise a new Flask object to a variable called app. web server will pass all the requests to this object under the WSGI protocol.

posts=[{'author':'sameed','title':'Blog post 1','content':'first post content','date':'Janurary 21,2018'},
{'author':'qazi','title':'Blog Post 2','content':'Second post content','date':'April 21,2018'}]


@app.route("/")
def index():
	return ""
 
@app.route("/home")
def hello():
	return render_template('home.html', posts=posts)
 
@app.route("/about")	
def members():
	return render_template('about.html', title='About')
 

if __name__ == "__main__":
	app.run(debug=True) 
#To check ,if this file is running directly
#to run our application with python directly



