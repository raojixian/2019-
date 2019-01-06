# coding:utf-8

import sqlite3

conn = sqlite3.connect('database/test.db')
c = conn.cursor()

print('open database success')

sql = c.execute("SELECT id,name,salary FROM USER")

for row in sql:
    print(row)

print('operation done successfully')
conn.close()

