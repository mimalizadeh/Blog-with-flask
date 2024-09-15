from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Mohammad'}

    posts = [
        {
            'author': {'username': "admin"},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': "admin"},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index/index.html", title="Home", user=user , posts=posts)
