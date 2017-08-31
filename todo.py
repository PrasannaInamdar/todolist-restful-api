from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api, reqparse

from resources.User import Register
from resources.item import Item, ItemList

from flask_jwt import JWT

from security import authenticate, identity

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Abcd@123456@localhost/learningflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api=Api(app)
app.secrete_key = 'Prasanna'




jwt = JWT(app, authenticate, identity)		

@app.route("/")
def Home():
	return render_template("home.html")

@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/signin")
def signin():
	return render_template("signin.html")

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/getdata", methods =['GET'])
def getdata():
	return {'tasks': list(map(lambda x:x.json(), ItemModel.query.all()	))}


api.add_resource(Item , '/item/<string:taskname>')
api.add_resource(Register, '/user') 
api.add_resource(ItemList, '/items')




if __name__ == '__main__':
	from db import db
	db.init_app(app)

app.run(debug=True)
