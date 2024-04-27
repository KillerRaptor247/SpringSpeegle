# dbSetup.py
# Establish Connection to the database
import pymysql
from app.dbConfig import mysql


def get_connection():
    try:
        connection = pymysql.connect(
            host=mysql['location'],
            user=mysql['user'],
            password=mysql['password'],
            database=mysql['database']
        )
        return connection
    except pymysql.Error as e:
        print(f"Error executing SQL query: {e}")
