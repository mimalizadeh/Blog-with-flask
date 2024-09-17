from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db



class User(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(64), index=True, unique=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String(64), index=True, unique=True)
    salt: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(256))
    password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(256))

    posts : orm.WriteOnlyMapped['Post'] = orm.relationship('Post', back_populates='author')

    create_at: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.utcnow)
    update_at: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"
