from app import db, lm
from werkzeug.security import generate_password_hash, check_password_hash


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class EmailLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is protected')

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'LoginEmail for user {} : {}'.format(self.user_id, self.email)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email_login = db.relationship('EmailLogin', uselist=False, backref='user')

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
