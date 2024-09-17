from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db
from .user import User


class Post(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(sa.String(140), default=None)
    body: orm.Mapped[str] = orm.mapped_column(sa.String(500))

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey('user.id'))
    author: orm.Mapped[User] = orm.mapped_column(sa.ForeignKey(User.id), index=True)

    create_at: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, nullable=False, default=datetime.utcnow,
                                                        index=True)
    update_at: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, nullable=False, default=datetime.utcnow,
                                                        onupdate=datetime.utcnow, index=True)

    def __repr__(self):
        return f'<Post({self.body})>'
