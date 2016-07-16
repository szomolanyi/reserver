from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
import logging
import logging.handlers
import logging.config
import json


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

with open('logging.json', 'rt') as f:
    log_config = json.load(f)
logging.config.dictConfig(log_config)

#logging.config.fileConfig('logging.ini')

#db_logger = logging.getLogger('sqlalchemy.engine')
#db_handler = logging.handlers.RotatingFileHandler('sql.log', backupCount=5, maxBytes=1024*1024)
#db_logger.addHandler(db_handler)
#db_logger.setLevel(logging.DEBUG)

#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


for MODULE in config.INSTALLED_MODULES:
    __import__(MODULE)


for rule in app.url_map.iter_rules():
    print rule
