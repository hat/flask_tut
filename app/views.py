from flask import render_template, flash, redirect, url_for
from app import app
from .forms import StaffForm
import os # favicon
from flask import send_from_directory # favicon
from flask import Flask, request # staff
from .models import Staff # staff
from app import db, models # staff

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/staff', methods=['GET', 'POST'])
def staff():
	form = StaffForm(request.form)
	staff = models.Staff.query.filter().all()
	if request.method == 'POST' and form.validate():
		staff = Staff(form.firstname.data, form.lastname.data, form.role.data,
					form.slack.data, form.email.data)
		db.session.add(staff)
		db.session.commit()
		flash('Staff member added')
		return redirect(url_for('staff'))
	return render_template('staff.html', title='Staff', form=form, staff=staff)

# @app.route('/guests', methods=['GET', 'POST'])
# def guests():
# 	form = GuestsForm(request.form)
# 	guest = models.Guests.query.filter().all()
# 	if request.method == 'POST' and form.validate():
# 		# Fill in Post
# 	return render_template('guest.html', title='Guests', form=form, guests=guests)

# Sets up favicon
@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon_cerberus', mimetype='image/vnd.microsoft.icon')