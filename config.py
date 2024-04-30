# config.py
# configuration file for Flask Environment
import os
from app.csi3335sp2023 import mysql


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'example-key-here'
    MYSQL_USER = mysql['user']
    MYSQL_PASSWORD = mysql['password']
    MYSQL_HOST = mysql['location']
    MYSQL_DB = mysql['database']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = "springspeegle2024@gmail.com"
    MAIL_PASSWORD = "kysj vqem cqqi ygpo"
    ADMINS = ['springspeegle2024@gmail.com']

