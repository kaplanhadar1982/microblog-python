from flask import Blueprint
api = Blueprint('api', __name__)

from app.api import index
from app.api import users
from app.api import post