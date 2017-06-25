from flask_wtf import Form
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired

class StaffForm(Form):
	firstname = StringField('firstname', [validators.Length(min=1, max=142)])
	lastname = StringField('lastname', [validators.Length(min=1, max=142)])
	role = StringField('role', [validators.Length(min=1, max=16)])
	slack = StringField('slack', [validators.Length(min=1, max=16)])
	email = StringField('email', [validators.Length(min=1, max=142)])