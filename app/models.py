from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(120), index=True, unique=True)
	lastname = db.Column(db.String(120), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	reason = db.Column(db.String(240), index=True)

	def __repr__(self):
		return '<User %r>' % (self.firstname)

# Example of another db model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)