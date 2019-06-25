# from flask import Flask

# from flask_sqlalchemy import SQLAlchemy
# # from database import db_session
# # from database import init_db
# # from models.user import User
# # from routes import *

# # Importing configs
# from config import config_dict

# app = Flask(__name__)

# # For the database
# db = SQLAlchemy()

# # @app.teardown_appcontext
# # def shutdown_session(exception=None):
# #     db_session.remove()

# if __name__ == '__main__':
#     # Enabling config initiation
#     app.config.from_object(config_dict['develop'])
#     config_dict['develop'].init_app(app)

#     db.init_app(app)
#     from api import api as api_blueprint
#     #init_db()
#     app.register_blueprint(api_blueprint, url_prefix='/api')
#     app.run(host='0.0.0.0', port=5000,debug=True)

    