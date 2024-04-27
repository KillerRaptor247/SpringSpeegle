#update2023.py
#update the current database with the 2023 data
import pymysql
from app.dbConfig import mysql

connection = pymysql.connect(host=mysql['location'],
                             user=mysql['user'],
                             password=mysql['password'],
                             db=mysql['database'])

#TODO UPDATE DATABASE WITH 2023 Teams Table and HallofFame Table