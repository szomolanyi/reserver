from flask import render_template
from flask_login import current_user
from app.main import main
from . import logger


@main.route('/')
def index():
    logger.debug('index start')
    return render_template('index.html')
