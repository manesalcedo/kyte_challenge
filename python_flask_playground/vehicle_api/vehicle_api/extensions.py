from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
cors = CORS()
csrf_protect = CSRFProtect()
migrate = Migrate()