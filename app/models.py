# models.py
# Establishes the ORM between the mysql database and SQLAlchemy
from typing import Optional
from time import time
import jwt
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login, app


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    is_admin: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)
    fav_team: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=True, default=None)

    # this tells python how to print out the User class!
    def __repr__(self):
        return 'User {}'.format(self.username)

    # Encrypt passwords!
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256'
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return db.session.get(User, id)


class Teams(db.Model):
    teams_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    teamID: so.Mapped[str] = so.mapped_column(sa.String(3), index=True, unique=True)
    yearID: so.Mapped[int] = so.mapped_column(sa.SmallInteger)
    team_name: so.Mapped[str] = so.mapped_column(sa.String(50))
    team_logo: so.Mapped[str] = so.mapped_column(sa.String(50), nullable=True, default=None)

    def __repr__(self):
        return 'Team {}'.format(self.teamID)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
