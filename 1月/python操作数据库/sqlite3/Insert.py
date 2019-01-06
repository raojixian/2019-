# coding:utf-8
import sqlite3
conn = sqlite3.connect('database/test.db')

c = conn.cursor()
print('open database successfully')

c.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY)"
          "VALUES(1,'RAOJIXIAN',32,'CHINA',2000.00)"
          )
c.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY)"
          "VALUES(2,'RAOJIXIAN',32,'CHINA',2000.00)"
          )
conn.commit()
print('records created successfully')
conn.close()
