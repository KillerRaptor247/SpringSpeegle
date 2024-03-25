# config.py
# configuration file for Flask Environment
import os
from Python_Scripts.dbConfig import mysql


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'example-key-here'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{mysql["user"]}:{mysql["password"]}@{mysql["host"]}/{mysql["database"]}'

