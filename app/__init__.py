from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from app.config import config_dict

# For the database
db = SQLAlchemy()
# For database migrations
migrate = Migrate()

bcrypt=Bcrypt()

def create_app(config_key='local'):
    app = Flask(__name__)
    
    # Enabling config initiation
    app.config.from_object(config_dict[config_key])
    config_dict[config_key].init_app(app)

    bcrypt.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.run(host='0.0.0.0', port=5000,debug=True)

    return app