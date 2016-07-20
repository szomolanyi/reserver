from flask import render_template
from flask_login import current_user
from app.main import main
from app import app


@main.route('/')
def index():
    app.logger.debug('index start')
    return render_template('index.html')
