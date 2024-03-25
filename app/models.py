#models.py
# Establishes the ORM between the mysql database and SQLAlchemy
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

#TODO CREATE ORM MODELS FOR EACH TABLE IN DATABASE
class User(db.Model):

