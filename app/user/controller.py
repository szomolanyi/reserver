from flask import logging, render_template, redirect, url_for
from flask_login import login_user, logout_user
from app.user import user
from app import app, db
from .forms import RegisterForm, LoginForm
from .model import User, EmailLogin


@user.route('/user')
def first():
    return "Ahoj svet"


@user.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        app.logger.debug('Register on submit')
        user = User()
        db.session.add(user)
        db.session.flush()
        app.logger.debug('User [{0}] created'.format(user.id))
        email_login = EmailLogin(
            email = form.email.data, 
            user_id = user.id
        )
        email_login.hash_password(form.password.data)
        db.session.add(email_login)
        db.session.commit()
        login_user(user)
        return(redirect(url_for('main.index')))
    return render_template('register.html', form=form)


@user.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email_login = EmailLogin.query.filter_by(email = form.email.data)[0]
        if email_login.verify_password(form.password.data):
            login_user(email_login.user)
            return(redirect(url_for('main.index')))
    return render_template('login.html', form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

