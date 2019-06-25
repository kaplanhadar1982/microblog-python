from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import config_dict

# For the database
db = SQLAlchemy()

def create_app(config_key='local'):
    app = Flask(__name__)
    # Enabling config initiation
    app.config.from_object(config_dict['develop'])
    config_dict['develop'].init_app(app)

    db.init_app(app)
    from app.api import api as api_blueprint
    #init_db()
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.run(host='0.0.0.0', port=5000,debug=True)

    return app