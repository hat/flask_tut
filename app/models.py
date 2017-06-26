from app import db
from datetime import datetime

class Staff(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(142), nullable=False)
	lastname = db.Column(db.String(142), nullable=False)
	role = db.Column(db.String(16))
	slack = db.Column(db.String(16))
	email = db.Column(db.String(142))

	def __init__(self, firstname, lastname, role, slack, email):
		self.firstname = firstname
		self.lastname = lastname
		self.role = role
		self.slack = slack
		self.email = email

	def __repr__(self):
		return '<User %r>' % (self.firstname)

class Guests(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(142), nullable=False)
	lastname = db.Column(db.String(142), nullable=False)
	timein = db.Column(db.DateTime, nullable=False)
	timeout = db.Column(db.DateTime)
	reason = db.Column(db.String(255))
	photo = db.Column(db.String(255))