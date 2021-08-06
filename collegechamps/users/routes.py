from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from flask_login import login_user, current_user, logout_user, login_required
from collegechamps import db, bcrypt
from collegechamps.users.forms import (RegistrationForm, LoginForm)
from collegechamps.models import User
from wtforms import ValidationError

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'succes')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form, login_register='Register')


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            # user = User.query.all()
            # name_of_user = user.username
            flash(
                f'Bravo {user.username}..We Welcome You To Our Website😍', 'succes')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Incorrect email or password!', 'error')
    return render_template('login.html', form=form)


@users.route("/logout")
def logout():
    logout_user()
    flash('You are logged out', 'info')
    return redirect(url_for('main.home'))
