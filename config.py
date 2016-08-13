import os
basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigBase:
    INSTALLED_MODULES = [
        'app.user.controller',
        'app.main.controller'
    ]

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'TODO SECRET'

    # debug settings
    EXPLAIN_TEMPLATE_LOADING = False

    # BOOTSTRAP
    BOOTSTRAP_SERVE_LOCAL = True


class DefaultConfig(ConfigBase):
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    # flask testing
    SQLALCHEMY_ECHO = True
    TESTING = True
    DEBUG = True  # Reloads after template change


class TestingConfig(ConfigBase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'testing.db')
    SQLALCHEMY_ECHO = False
    # flask testing
    TESTING = True
    WTF_CSRF_ENABLED = False


config = {
    'default': DefaultConfig,
    'test': TestingConfig
}
