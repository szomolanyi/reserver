from flask import Blueprint
import logging


logger = logging.getLogger(__name__)
main = Blueprint('main', __name__, template_folder='templates')

import controller
