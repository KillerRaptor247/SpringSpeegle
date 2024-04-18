# config.py
# configuration file for Flask Environment
import os
from Python_Scripts.dbConfig import mysql


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'example-key-here'
    MYSQL_USER = mysql['user']
    MYSQL_PASSWORD = mysql['password']
    MYSQL_HOST = mysql['location']
    MYSQL_DB = mysql['database']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

