from db import db

class ItemModel(db.Model):
	__tablename__='tasks'
	uid = db.Column(db.Integer, primary_key = True)
	taskname = db.Column(db.String(100))


	def __init__(self, taskname):
		self.taskname=taskname

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()

	def json(self):
		return {'uid': self.uid, 'taskname':self.taskname }

	@classmethod
	def find_by_name(cls, taskname):
		return cls.query.filter_by(taskname=taskname).first()

	@classmethod
	def find_by_id(cls,_id):
		return cls.query.filter_by(id=_id).first()
