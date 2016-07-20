from flask import Blueprint

user = Blueprint('user', __name__, template_folder = 'templates')

import controller
import model

from app import app



app.register_blueprint(user)

