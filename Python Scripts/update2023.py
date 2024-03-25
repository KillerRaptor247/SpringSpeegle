#update2023.py
#update the current database with the 2023 data
import pymysql
from dbConfig import mysql

connection = pymysql.connect(host=mysql['host'],
                             user=mysql['user'],
                             password=mysql['password'],
                             db=mysql['database'])

#TODO UPDATE DATABASE WITH 2023 BASEBALL DATA