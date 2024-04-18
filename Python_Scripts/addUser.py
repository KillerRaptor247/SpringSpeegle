# addUser.py
# Python File to add the User table to the database

import pymysql
from werkzeug.security import generate_password_hash

from dbConfig import mysql

connection = pymysql.connect(host=mysql['host'],
                             user=mysql['user'],
                             password=mysql['password'],
                             db=mysql['database'])

#TODO ADD USER TABLE TO DATABASE
cur = connection.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users ("
            "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,"
            "username VARCHAR(20) NOT NULL,"
            "email VARCHAR(64) NOT NULL UNIQUE,"
            "password_hash VARCHAR(128) NOT NULL,"
            "is_admin BOOLEAN NOT NULL DEFAULT FALSE);")

#TODO ADD ADMIN USER AND INSERT
hash = generate_password_hash('BaseballRocks')
sql = "INSERT INTO users (username, email, password_hash, is_admin) " \
        "VALUES ('TheSpeegle', 'Greg@FakeEmail.com', %s, True)"
cur.execute(sql, (hash,))
connection.commit()
cur.close()
connection.close()

