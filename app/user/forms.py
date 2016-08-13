# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flask_babel import gettext
from .model import EmailLogin


def validate_email(form, field):
    u = EmailLogin.query.filter_by(email=field.data)
    if u.count() > 0:
        raise ValidationError(
            gettext("User with email address {} already exists".format(field.data)))


class RegisterForm(Form):
    email = StringField('Enter your email', validators=[
                        DataRequired(), Email(), validate_email])
    password = PasswordField('Enter your password', validators=[
                             DataRequired(), Length(min=8, max=50)])
    password2 = PasswordField('Repeat your password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField('Login')
