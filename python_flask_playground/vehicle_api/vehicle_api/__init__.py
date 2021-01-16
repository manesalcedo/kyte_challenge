from flask import Flask, json
from vehicle_api.config import Config

from vehicle_api.extensions import (
    cors,
    db,
    csrf_protect,
    migrate,
)

__title__ = 'Vehicle API'
__author__ = 'Maria'
__license__ = ''

def create_app():
    application = Flask(__name__)
    application.config.from_object(Config)
    
    db.init_app(application)
    cors.init_app(application)
    migrate.init_app(application, db)

    with application.app_context():
        from vehicle_api.app.utils import utils_app
        from vehicle_api.app.vehicle import vehicle_app
        application.register_blueprint(app.utils.utils_app)
        application.register_blueprint(app.vehicle.vehicle_app)
        
    with application.test_client() as c:
        resp = c.get('/api/vehicles?sort=model&status=available&model=Versa&page=2&per_page=1')
        data = json.loads(resp.data)
        assert data['data'][0]['license_plate_number'] == '8SAJ753'

    with application.test_client() as c:
        resp = c.get('/api/vehicles?sort=model&status=available&model=Versae&page=2&per_page=1')
        data = json.loads(resp.data)
        assert data['data'] == []

    with application.test_client() as c:
        resp = c.get('/api/vehicles')
        data = json.loads(resp.data)
        assert data['meta']['per_page'] == 20
        assert data['meta']['page'] == 1
        assert data['data'][0]['license_plate_number'] == '1DMP23'
    
    with application.test_client() as c:
        resp = c.get('/api/vehicles?invalid_filter=invalid_filter')
        data = json.loads(resp.data)
        assert data['meta']['per_page'] == 20
        assert data['meta']['page'] == 1
        assert data['data'][0]['license_plate_number'] == '1DMP23'

    return application




