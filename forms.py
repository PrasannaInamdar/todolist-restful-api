from flask_wtf import Form 
from wtforms import StringField, SubmitField

class IndexForm(Form):
  taskname = StringField('addMe')
  submit = SubmitField('Sign up')
  searchname = StringField('SearchMe')