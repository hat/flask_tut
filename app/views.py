from flask import render_template, flash, redirect, url_for
from app import app
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
	staff = models.Staff.query.filter().all()
	if request.method == 'POST':
		staff = Staff()
		staff.firstname = request.form.get('firstname').capitalize()
		staff.lastname = request.form.get('lastname').capitalize()
		staff.role = request.form.get('role').capitalize()
		staff.slack = request.form.get('slack')
		staff.email = request.form.get('email')
		db.session.add(staff)
		db.session.commit()
		flash('Staff member added')
		return redirect(url_for('staff'))
	return render_template('staff.html', title='Staff', staff=staff)

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
	return render_template('guests.html', date=datetime.now().isoformat(), title='Guests', guests=guests)

@app.route('/guests_timeout/<int:guest_id>', methods=['GET', 'POST'])
def guests_timeout(guest_id):
	if request.method == 'POST':
		Guests.query.filter_by(id=guest_id).update(dict(timeout=datetime.now()))
		db.session.commit()
	return redirect(url_for('guests'))

@app.route('/guests_delete/<int:guest_id>', methods=['GET', 'POST'])
def guests_delete(guest_id):
	if request.method == 'POST':
		Guests.query.filter_by(id=guest_id).delete()
		db.session.commit()
	return redirect(url_for('guests'))


# Sets up favicon
@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon_cerberus', mimetype='image/vnd.microsoft.icon')