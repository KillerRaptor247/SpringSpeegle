# addUser.py
# Python File to add the User table to the database

import pymysql
from werkzeug.security import generate_password_hash

from . import dbConfig as dbC


def insertAdmin():
    connection = pymysql.connect(host=dbC.mysql['location'],
                                 user=dbC.mysql['user'],
                                 password=dbC.mysql['password'],
                                 db=dbC.mysql['database'])
    cur = connection.cursor()

    hash = generate_password_hash('BaseballRocks')
    sql = "REPLACE INTO user (id, username, email, password_hash, is_admin, fav_team) " \
          "VALUES (100,'TheSpeegle', 'Greg@FakeEmail.com', %s, True, 'Detroit Tigers')"
    cur.execute(sql, (hash,))
    connection.commit()
    cur.close()
    connection.close()

