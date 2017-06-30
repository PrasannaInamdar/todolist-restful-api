from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db1 = SQLAlchemy()


class User(db.Model):
	__tablename__='tasks'
	uid=db.Column(db.Integer, primary_key = True)
	taskname = db.Column(db.String(100))



	def __init__(self,taskname):
		self.taskname=taskname

