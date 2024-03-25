# addUser.py
# Python File to add the User table to the database

import pymysql
from dbConfig import mysql

connection = pymysql.connect(host=mysql['host'],
                             user=mysql['user'],
                             password=mysql['password'],
                             db=mysql['database'])

#TODO ADD USER TABLE TO DATABASE

