#DATABASE
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

__author__ = 'tony'


class Config():
    APP_FOLDER = '/home/webmaster/security/'
    DATABASE_HOST = 'security-host.42.us.org'
    DATABASE_NAME = 'main'
    DATABASE_USER = 'security'
    DATABASE_PASSWORD = 'hjd8fn239dj29dj92dj29jd29dj2'
    UPLOAD_FOLDER = '/home/webmaster/nostromo/app/static/uploads/'
    CRYPT_KEY = 'gBenh6sQxtQsYfU2iqzKhSq3e1tWbA'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=False
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s/%s' % (DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME)
    SQLALCHEMY_BINDS = {
        'database': 'postgres://%s:%s@%s/database' % (DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST),
        'main': 'postgres://%s:%s@%s/main' % (DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST),
        'stats': 'postgres://%s:%s@bigbrother-sql.42.us.org/stats' % ('stats', 'fdASmn301OOKdmnv32c563VF')
    }