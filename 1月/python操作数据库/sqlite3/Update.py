# coding:utf-8

import sqlite3

conn = sqlite3.connect('database/test.db')

c = conn.cursor()
print('ok')

cursor = conn.execute("UPDATE USER SET SALARY = 100 WHERE ID = 1")
conn.commit()
print('done')



