import os
basedir = os.path.abspath(os.path.dirname(__file__))

INSTALLED_MODULES = [
    'app.user.controller',
    'app.main.controller'
]

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'TODO SECRET'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False
#ECHO = True

# debug settings
EXPLAIN_TEMPLATE_LOADING=True
