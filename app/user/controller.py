from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.user import user
from app import db
from .forms import RegisterForm, LoginForm
from .model import User, EmailLogin
from . import logger


@user.route('/profile')
def profile():
    return "Ahoj svet"


@user.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        logger.debug('Register on submit')
        user = User()
        db.session.add(user)
        db.session.flush()
        logger.debug('User [{0}] created'.format(user.id))
        email_login = EmailLogin(
            email=form.email.data,
            user_id=user.id,
            password=form.password.data
        )
        db.session.add(email_login)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.index'))
    else:
        return render_template('register.html', form=form)


@user.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        logger.debug('Email login for {0}'.format(form.email.data))
        email_logins = EmailLogin.query.filter_by(email=form.email.data).all()
        if len(email_logins) == 1:
            email_login = email_logins[0]
        else:
            email_login = None
        if email_login and email_login.verify_password(form.password.data):
            login_user(email_login.user)
            return(redirect(url_for('main.index')))
        else:
            flash('Invalid username or password')
            return(redirect(url_for('user.login')))
    return render_template('login.html', form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
