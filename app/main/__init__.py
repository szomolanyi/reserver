from flask import Blueprint


main = Blueprint('main', __name__, template_folder = 'templates')

import controller

from app import app

app.register_blueprint(main)

