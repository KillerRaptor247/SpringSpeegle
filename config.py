# config.py
# configuration file for Flask Environment
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'example-key-here'
