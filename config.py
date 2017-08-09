#DATABASE
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

__author__ = 'tony'


class Config(object):
    DEBUG = False
    TESTING = False
    APP_FOLDER = '/home/webmaster/security/'
    DATABASE_HOST = 'security-host.42.us.org'
    DATABASE_NAME = 'main'
    DATABASE_USER = 'security'
    DATABASE_PASSWORD = 'hjd8fn239dj29dj92dj29jd29dj2'
    UPLOAD_FOLDER = '/home/webmaster/nostromo/app/static/uploads/'
    CRYPT_KEY = 't6hgfjhsfiu1781LJGF83fusF3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s/%s' % (DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME)

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True