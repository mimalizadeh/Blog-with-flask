from app import app

from flask import render_template, flash, redirect, url_for

from app.forms.login import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login request for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))

    return render_template("auth/login.html", title="Login", form=form)
