from flask import Blueprint
from flask_login import LoginManager
import logging


user = Blueprint('user', __name__, template_folder = 'templates')

logger = logging.getLogger(__name__)

import controller
import model
