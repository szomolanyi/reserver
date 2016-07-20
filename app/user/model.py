from app import db, lm
from passlib.apps import custom_app_context as pwd_context


class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    street_address = db.Column(db.String(255))
    town = db.Column(db.String(255))
#    email_login_ = db.relationship('EmailLogin', uselist=False, backref='provider')

    def __repr__(self):
        return "Provider {} on {}".format(self.name, self.street_address)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class EmailLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return 'LoginEmail for user {} : {}'.format(self.user_id, self.email)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email_login = db.relationship('EmailLogin', uselist = False, backref = 'user')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3