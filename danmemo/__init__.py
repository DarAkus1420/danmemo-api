__version__ = '0.1.0'
from flask import Flask

from .models import db

from .views import api_v2
app = Flask(__name__)

def create_app(environment):
    
    app.config.from_object(environment)
    
    app.register_blueprint(api_v2)
    
    with app.app_context():
        db.init_app(app)
    
    return app
