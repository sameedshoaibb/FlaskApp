from flask import render_template, url_for,flash, redirect, request 
from main_app import app,db,bcrypt  
from main_app.models import User,Post
from main_app.forms import RegistrationForm,LoginForm, UpdateAccountForm
from flask_login import login_user,current_user,logout_user,login_required 

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
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm() #Create instance
	
	#register first time user in the database, with the password in the hashed 
	if form.validate_on_submit():
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.data, email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your Account has been created. You can now log in for {}'.format(form.username.data),'success')
		return redirect(url_for('login'))

	return render_template('register.html', title='register', form=form)
 
@app.route("/login", methods=['GET','POST'])	
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm() #Create instance
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data): #if email exists and password is valid
			#then log the user in
			#import login user function
			login_user(user,remember=form.remember.data)
			next_page= request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessfull. Please check email and password','danger')
	return render_template('login.html', title='Login', form=form) 


@app.route("/logout")	
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route("/account", methods=['GET','POST'])	
@login_required
def account():
	form=UpdateAccountForm()
	if form.validate_on_submit():
		current_user.username=form.username.data
		current_user.email=form.email.data
		db.session.commit()
		flash("Your account has been updated","success")
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data=current_user.username
		form.email.data=current_user.email

	image_file= url_for('static',filename='profile_pics/'+current_user.image_file)
	return render_template('account.html', title='Account',image_file=image_file, form=form)
