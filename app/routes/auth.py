from app import app, db

from flask import render_template, flash, redirect, url_for

from app.forms.login import LoginForm
from app.models.user import User
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
import sqlalchemy.orm as orm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user_model = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))

        if user_model in None or not user_model.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user_model, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template("auth/login.html", title="Login", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
