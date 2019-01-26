from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME']= 'connect_to_mongo'
app.config['MONGO_URI']= 'mongodb://sameed:explode1234567--x@ds163984.mlab.com:63984/connect_to_mongo'

mongo = PyMongo(app)

@app.route("/home")
def home():
	user = mongo.db.users
	user.insert({'name':'Jaffer', 'language':'python'})
	user.insert({'name':'hamdani', 'language':'C'})
	user.insert({'name':'symond', 'language':'gad'})
	user.insert({'name':'Ibless', 'language':'golang'})
	return "Added user"

if __name__ == "__main__": #to run our application when python directly calls main_app.py. It will not run, when other file  will import this. 
	app.run()


from main_app_copy import db
db.create_all()
from main_app_copy import User, Post
user_11= User(username='1Corey1',email='1c1',password='1s')
db.session.add(user_11)
user_22= User(username='11C1orey',email='1c11',password='s11')
db.session.add(user_22)
db.session.commit()
User.query.all()
