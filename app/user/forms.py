# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, BooleanField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flask_babel import gettext
from .model import EmailLogin



def validate_user_exists(form, field):
    u=EmailLogin.query.filter_by(email=field.data)
    if u.count()==0:
        raise ValidationError(gettext("User with email %(user)s not found", user=field.data))



class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password')
    remember_me = BooleanField('remember_me', default=False)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        u=EmailLogin.query.filter_by(email=self.email.data)
        if u.count()==0:
            self.email.errors.append(gettext("User with email %(user)s not found", user=self.email.data))
            return False
        if not u[0].verify_password(self.password.data):
            return False



def validate_email(form, field):
    u=EmailLogin.query.filter_by(email=field.data)
    if u.count()>0:
        raise ValidationError("email {} is already used".format(field.data))


class RegisterForm(Form):
    email=StringField('email', validators=[DataRequired(), validate_email])
    password=StringField('name')
