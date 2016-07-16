from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_TRACK_MODIFICATIONS
from app import db
from app import app

print app.config['SQLALCHEMY_DATABASE_URI']

import os.path
db.create_all()
