from flask import Blueprint
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

user = Blueprint('user', __name__)

import controller
import model

from app import app, db

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, model.EmailLogin, model.Role)
security = Security(app, user_datastore)


app.register_blueprint(user)

