from flask import Flask, render_template , Response	
from flask import request , jsonify
from flask_sqlalchemy import SQLAlchemy
from message import client
import json
import logging
import sys
from flask_heroku import Heroku

import os
                                                                             

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Abcd@123456@localhost/learningflask'


heroku= Heroku(app)
db = SQLAlchemy(app)



class User(db.Model):
	__tablename__='tasks'
	uid=db.Column(db.Integer, primary_key = True)
	taskname = db.Column(db.String(100))

	def __init__(self,taskname):
		self.taskname=taskname



@app.route("/")
def index():
	return render_template("index.html",User=User.query.all())

@app.route("/getdata", methods=['GET'])
def get_User(): 
	myuser=User.query.all()
	if myuser=="":
		return 404
	return Response(json.dumps({'taskname':[user.taskname for user in myuser]}),  mimetype='application/json')



@app.route('/', methods=['POST'])
def my_form_post():
	

		text=request.form['text']
		if text !="":
			newuser = User(text)
			db.session.add(newuser)
			db.session.commit()
			message = client.messages.create(
			to="+15122105811", 	from_="+17734327410" , body ="A task has been added to your todo list :  "+ text)
			print(message.sid)
			return render_template("index.html",User=User.query.all())
				
		else:	
			newuser = request.form.getlist('removeId')
			if newuser:
				for n in newuser:
					User.query.filter_by(uid=n).delete()
				db.session.commit()
				return render_template("index.html",User=User.query.all())
			else:
				edituser = request.form.getlist('editId')
				if edituser:
					updatedText=request.form['updatedText']
					for e in edituser:
						User.query.filter_by(uid=e).update(dict(taskname=updatedText))
					db.session.commit()
					return render_template("index.html",User=User.query.all())


if __name__ == "__main__":
	app.run(debug=True)	 
	

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

