from flask import render_template, flash, redirect, url_for
from app import app
from .forms import StaffForm, GuestsForm
import os # favicon
from flask import send_from_directory # favicon
from flask import Flask, request # staff
from .models import Staff, Guests # staff, guests
from app import db, models # staff
from datetime import datetime # guests

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

@app.route('/guests', methods=['GET', 'POST'])
def guests():
	guests = models.Guests.query.filter().all()
	if request.method == 'POST':
		guest = Guests()
		guest.firstname = request.form.get('firstname')
		guest.lastname = request.form.get('lastname')
		guest.timein = datetime.now()
		guest.reason = request.form.get('reason')
		db.session.add(guest)
		db.session.commit()
		flash('Guest added')
		return redirect(url_for('guests'))
	return render_template('guests.html', title='Guests', guests=guests)

# Sets up favicon
@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon_cerberus', mimetype='image/vnd.microsoft.icon')