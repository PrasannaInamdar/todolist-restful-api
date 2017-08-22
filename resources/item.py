from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from db import db
from models.item import ItemModel
from flask_jwt import JWT, jwt_required



class Item(Resource):
	parser = reqparse.RequestParser()
	
	parser.add_argument('taskname',
		type=str,
		required=True,
		help="This field can not be left blank"
		)

	@jwt_required()
	def get(self, taskname):
		item = ItemModel.find_by_name(taskname)
		if item:	
			return item.json()
		return {'messege':'Item not found'},404

	def post(self, taskname):
		if ItemModel.find_by_name(taskname):
			return {'messege':"An item already exists!"}, 400

		
		work = ItemModel(taskname)
		
		try:
			work.save_to_db()
			return {"messege":"Task added successfully!"}
		
		except:
			return {"messege":"An error occurred saving a task!"}

		return work.json(), 201

	def delete(self, taskname):
		task = ItemModel.find_by_name(taskname)
		if task:
			task.delete_from_db()
		return {"messege":"task is deleted"}


	def put(self, taskname):
		data = Item.parser.parse_args()
		task = ItemModel.find_by_name(taskname)
		if task:
			task.taskname = data['taskname']
		task.save_to_db()
		return task.json()




class ItemList(Resource):
	def get(self):
		return {'tasks':list(map(lambda x:x.json(), ItemModel.query.all()	))}