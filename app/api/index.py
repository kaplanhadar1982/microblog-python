from app.api import api

@api.route('/')
def index():
    return 'hello router'