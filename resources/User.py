from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from db import db
from models.User import UserModel


class Register(Resource):
	parser = reqparse.RequestParser()
	

	parser.add_argument('username',
		type=str,
		required=True,
		help="This field can not be left blank"
		)

	parser.add_argument('password',
		type=str,
		required = True,
		help="This field can not be left blank"
		)

	def post(self):
		data = Register.parser.parse_args()
		reguser = UserModel(data['username'],data['password'])
		
		try:
			UserModel.save_to_db(reguser)
			return {"messege":"User registered successfully!"}
		
		except:
			return {"messege":"An error occurred registering user!"}

	def get(self):
		return "I am working"