# models.py
# Establishes the ORM between the mysql database and SQLAlchemy
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login


# TODO CREATE ORM MODELS FOR EACH TABLE IN DATABASE
class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    is_admin: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)

    # this tells python how to print out the User class!
    def __repr__(self):
        return 'User {}'.format(self.username)

    # Encrypt passwords!
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Teams(db.Model):

    teams_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    teamID: so.Mapped[str] = so.mapped_column(sa.String(3), index=True, unique=True)
    yearID: so.Mapped[int] = so.mapped_column(sa.SmallInteger)
    team_name: so.Mapped[str] = so.mapped_column(sa.String(50))

    def __repr__(self):
        return 'Team {}'.format(self.teamID)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
