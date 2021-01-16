import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HEALTH_API = '/api/health'
    VEHICLE_API = '/api/vehicles'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False