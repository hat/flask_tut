#FLASK

##Set Up
- Directory
	1. app
	2. app/static
	3. app/templates - html template files
	4. tmp

- Files
	1. config.py - configuration of database, forms, etc...
	2. run.py - file to run flask
	3. requirements.txt - pip installs *pip install -r requirements.txt*
	3. /app/__init__.py - imports and config
	4. /app/views.py - redirects of pages

- Imports
	* flask_wtf - forms for input
	* flask_sqlalchemy - sql database

- Database
	* apps/models.py - database structure
	* db_create.py - script to create
	* db_migrate.py - script to migrate for db changes
	
	