from app import app, db
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.models import user, post


@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'db': db, 'orm': orm, 'User': user.User, 'Post': post.Post}
