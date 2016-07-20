from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
import config
import logging
import logging.handlers
import logging.config
import json


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)

babel = Babel(app)

with open('logging.json', 'rt') as f:
    log_config = json.load(f)
logging.config.dictConfig(log_config)


for MODULE in config.INSTALLED_MODULES:
    __import__(MODULE)


for rule in app.url_map.iter_rules():
    print rule
