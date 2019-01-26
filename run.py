#!/usr/bin/python

from main_app import app

if __name__ == "__main__": #to run our application when python directly calls main_app.py. It will not run, when other file  will import this. 
	app.run(debug=True) #To run the flask app on particular instance  





