# coding:utf-8

import sqlite3
import connect
file = 'database/test.db'
conn = connect.connectDatabase(file)
print('open database')
c = conn.cursor()
c.execute('''
    CREATE TABLE USER(
    ID INT PRIMARY KEY NOT NULL,
    NAME  TEXT NOT NULL,
    AGE  INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
    );
''')
print('table create successfuly')
conn.commit()
conn.close()


