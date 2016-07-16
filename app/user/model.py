from app import db
from flask_security import UserMixin, RoleMixin


class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    street_address = db.Column(db.String(255))
    town = db.Column(db.String(255))
#    email_login_ = db.relationship('EmailLogin', uselist=False, backref='provider')

    def __repr__(self):
        return "Provider {} on {}".format(self.name, self.street_address)


# class EmailLogin(db.Model):
#    email = db.Column(db.String(500), primary_key=True)
#    token = db.Column(db.String(500))
#    provider_id = db.Column(db.Integer, db.ForeignKey("provider.id"))
#    provider_ = db.relationship('Provider', backref='emaillogin')


# flask security model
roles_users = db.Table('roles_users',
                       db.Column('login_id', db.Integer(),
                                 db.ForeignKey('email_login.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class EmailLogin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('EmailLogin', lazy='dynamic'))
