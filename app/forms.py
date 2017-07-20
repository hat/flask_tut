from datetime import datetime

class StaffForm(Form):
	firstname = StringField('firstname', [validators.Length(min=1, max=142)])
	lastname = StringField('lastname', [validators.Length(min=1, max=142)])
	role = StringField('role', [validators.Length(min=1, max=16)])
	slack = StringField('slack', [validators.Length(min=1, max=16)])
	email = StringField('email', [validators.Length(min=1, max=142)])

class GuestsForm(Form):
	firstname = StringField('firstname', [validators.Length(min=1, max=142)])
	lastname = StringField('lastname', [validators.Length(min=1, max=142)])
	timein = DateTimeField('timein', format='%Y-%m-%d %H:%M:%S', default=datetime.now(), validators=[validators.DataRequired()])
	timeout = DateTimeField('timeout', format='%Y-%m-%d')
	reason = StringField('reason', [validators.Length(min=1, max=255)])
	photo = StringField('photo', [validators.Length(min=1, max=255)])