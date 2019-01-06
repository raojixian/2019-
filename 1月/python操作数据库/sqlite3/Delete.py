# coding:utf-8

import sqlite3

conn = sqlite3.connect('database/test.db')
c = conn.cursor()

print('ok ')
c.execute("DELETE FROM USER WHERE ID = 2")
conn.commit()
print('done')