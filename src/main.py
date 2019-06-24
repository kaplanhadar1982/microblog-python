from flask import Flask

from database import db_session
from database import init_db
from models.user import User
from routes import *

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.register_blueprint(routes)
    app.run(host='0.0.0.0', port=5000,debug=True)