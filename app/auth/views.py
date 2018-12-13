from flask import render_template, redirect, url_for
from app.models import User
from . import auth
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(number=form.number.data).first()
        if user is not None:
            login_user(user)
            return redirect(url_for('project.index'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('project.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    number=form.number.data,
                    password=form.password.data)
        db.session.add(user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
