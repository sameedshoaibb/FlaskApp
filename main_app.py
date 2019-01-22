#!/usr/bin/python

#To run flask app with environment variable
#export set FLASK_APP=main_app.py
#export set FLASK_DEBUG=1
#flask run

from flask import Flask, render_template, url_for,flash, redirect 	    
from forms import RegistrationForm,LoginForm
app = Flask(__name__) #initialise a new Flask object to a variable called app. web server will pass all the requests to this object under the WSGI protocol.

#To setup a secret key from cyber attacks such as csrf -->
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'

posts=[{'author':'sameed','title':'Blog post 1','content':'first post content','date':'Janurary 21,2018'},
{'author':'qazi','title':'Blog Post 2','content':'Second post content','date':'April 21,2018'}]

# A decorator, which url to be associated to which function.
@app.route("/")
def index():
	return render_template('home.html', posts=posts)
 
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)
 
@app.route("/about")	
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])	
def register():
	form = RegistrationForm() #Create instance
	if form.validate_on_submit():
		flash('Account created for {}'.format(form.username.data),'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='register', form=form)
 
@app.route("/login", methods=['GET','POST'])	
def login():
	form = LoginForm() #Create instance
	if form.validate_on_submit():
		if form.email.data=='admin@blog.com' and form.password.data=='':
			flash('Yao have been logged in!','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessfull. Please check username and password','danger')
	return render_template('login.html', title='Login', form=form) 

if __name__ == "__main__": #to run our application when python directly calls main_app.py. It will not run, when other file  will import this. 
	app.run(debug=True) #To run the flask app on particular instance  





