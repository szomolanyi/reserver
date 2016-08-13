from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import config
import logging
import logging.handlers
import logging.config
import json


db = SQLAlchemy()
babel = Babel()
lm = LoginManager()


with open('logging.json', 'rt') as f:
    log_config = json.load(f)
    logging.config.dictConfig(log_config)


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_object(config.config[cfg])

    Bootstrap(app)
    db.init_app(app)
    babel.init_app(app)
    lm.init_app(app)

    from .user import user
    app.register_blueprint(user)

    from .main import main
    app.register_blueprint(main)

    return app
